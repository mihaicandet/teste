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