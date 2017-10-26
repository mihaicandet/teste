# coding=utf-8
from odoo import models, fields, api


class AsistentaSocialaDosar(models.Model):
    _name = 'asistenta.dosar'
    _description = "Dosar"
    _inherit = 'mail.thread'

    name = fields.Char(string="Nr dosar")
    state = fields.Selection(
        [('draft', 'Cerere'), ('ancheta', 'Ancheta'), ('aprobat', 'Aprobata'), ('respins', 'Respins')],
        string='Status', index=True, default='draft', copy=False)

    date = fields.Date()
    reprezentant = fields.Boolean()

    solicitant_id = fields.Many2one('res.partner', string="Solicitant", domain=[('is_company', '=', False)])
    solicitant_cnp = fields.Char(related="solicitant_id.cnp")
    solicitant_id_nr = fields.Char(related="solicitant_id.id_nr")
    solicitant_id_tip = fields.Selection(related="solicitant_id.id_tip")
    solicitant_city = fields.Char(related="solicitant_id.city")
    solicitant_street = fields.Char(related="solicitant_id.street")
    solicitant_state_id = fields.Many2one("res.country.state", related="solicitant_id.state_id")
    solicitant_zip = fields.Char(related="solicitant_id.zip")
    solicitant_country_id = fields.Many2one('res.country', related="solicitant_id.country_id")

    persoana_id = fields.Many2one('res.partner', string="Persoana indreptatita", domain=[('is_company', '=', False)])

    cnp = fields.Char(related="persoana_id.cnp")
    id_tip = fields.Selection(related="persoana_id.id_tip")
    id_nr = fields.Char(related="persoana_id.id_nr")
    city = fields.Char(related="persoana_id.city")
    street = fields.Char(related="persoana_id.street")
    state_id = fields.Many2one("res.country.state", related="persoana_id.state_id")
    zip = fields.Char(related="persoana_id.zip")
    country_id = fields.Many2one('res.country', related="persoana_id.country_id")

    membru_ids = fields.One2many('asistenta.membru', 'dosar_id')
    venit_ids = fields.One2many('asistenta.venit', 'dosar_id')

    # stare locativa
    tip_gospodarie = fields.Selection([('singura', 'Singura'), ('pers', 'Impreună altă persoană singură'),
                                       ('fam', 'Impreună cu altă familie')])

    tip_locuinta = fields.Selection([('A', 'Tip A'), ('B', 'Tip B')])
    tip_casa = fields.Selection([
        ('curte', 'Casă cu curte'), ('fara_curte', 'Casă fara curte'), ('fara', 'Nu are locuinţă'),
        ('nec', 'Locuinţă de necesitate'), ('inst', 'Instituţionalizat'), ('bloc', 'Apartament la bloc'),
        ('serviciu', 'Locuinţă de serviciu')
    ])

    @api.onchange('solicitant_id')
    def _onchange_solicitant_id(self):
        if self.solicitant_id:
            if not self.reprezentant and self.solicitant_id != self.persoana_id:
                self.persoana_id = self.solicitant_id
            else:
                if not self.persoana_id:
                    self.persoana_id = self.solicitant_id

    @api.onchange('persoana_id')
    def _onchange_persoana_id(self):
        if self.persoana_id:
            if not self.reprezentant and self.solicitant_id != self.persoana_id:
                self.solicitant_id = self.persoana_id
            else:
                if not self.solicitant_id:
                    self.solicitant_id = self.persoana_id


class AsistentaSocialaMembru(models.Model):
    _name = 'asistenta.membru'
    _description = "Membru Familie"

    dosar_id = fields.Many2one('asistenta.dosar')
    persoana_id = fields.Many2one('res.partner', string="Persoana", domain=[('is_company', '=', False)])
    cnp = fields.Char(related="persoana_id.cnp")

    id_tip = fields.Selection(related="persoana_id.id_tip")
    id_nr = fields.Char(related="persoana_id.id_nr")

    city = fields.Char(related="persoana_id.city")
    street = fields.Char(related="persoana_id.street")
    country_id = fields.Many2one('res.country', related="persoana_id.country_id")

    relatie = fields.Selection([('copil', 'Copil'), ('adult', 'Adult')])
    situatie_scolara = fields.Selection(related="persoana_id.situatie_scolara")
    situatie_prof = fields.Selection(related="persoana_id.situatie_prof")
    scoala = fields.Many2one('res.partner', related="persoana_id.scoala")
    asistenta_sociala = fields.Boolean()


class AsistentaSocialaBun(models.Model):
    _name = 'asistenta.bun'
    _description = "Bunuri"

    dosar_id = fields.Many2one('asistenta.dosar')
    categ_id = fields.Many2one('asistenta.categ.bun')
    venit = fields.Float()


class AsistentaSocialaVenit(models.Model):
    _name = 'asistenta.venit'
    _description = "Venituri"

    dosar_id = fields.Many2one('asistenta.dosar')
    categ_id = fields.Many2one('asistenta.categ.venit')
    venit = fields.Float()


class AsistentaSocialaCategVenit(models.Model):
    _name = 'asistenta.categ.venit'
    _description = "Categorie Venituri"

    name = fields.Char()
    cod = fields.Char()
    grupa_id = fields.Many2one('asistenta.grupa.categ.venit')
    tip_act = fields.Char()


class AsistentaSocialaGrupaCategVenit(models.Model):
    _name = 'asistenta.grupa.categ.venit'
    _description = "Grupa Categorie Venituri"

    name = fields.Char()


class AsistentaSocialaCategBun(models.Model):
    _name = 'asistenta.categ.bun'
    _description = "Categorie Bunuri"

    name = fields.Char()
    cod = fields.Char()
    grupa_id = fields.Many2one('asistenta.grupa.categ.bun')
    value = fields.Float()


class AsistentaSocialaGrupaCategBun(models.Model):
    _name = 'asistenta.grupa.categ.bun'
    _description = "Grupa Categorie Bun"

    name = fields.Char()
