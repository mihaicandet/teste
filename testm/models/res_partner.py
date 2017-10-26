# coding=utf-8

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    este_scoala = fields.Boolean()

    stare_civila = fields.Selection([
        ('', 'Necompletat'), ('n', 'Necăsatorit'), ('d', 'Divorțat'),
        ('v', 'Vaduv'), ('u', 'Uniune consensuală')
    ])

    id_tip = fields.Selection([
        ('B.I.', 'buletin de identitate'),
        ('C.I.', 'carte de identitate'),
        ('C.I.P.', 'carte de identitate provizorie'),
        ('P.', 'paşaport'),
        ('P.S.T.', 'permis de şedere temporară'),
        ('P.S.P.', 'permis de şedere permanentă'),
        ('D.I.', 'document de identitate'),
        ('CR ', 'carte de rezidenţă'),
        ('CRP', 'carte de rezidenţă permanentă')], default='C.I.',  string="Tip act"
    )


    situatie_scolara = fields.Selection([('', 'Necompletat'),
                                         ('fara', 'Fara studii'), ('elev', 'Elev'), ('student', 'Student'),
                                         ('generale', 'Generale'), ('medii', 'Medii'), ('superioare', 'Superioare')
                                         ], string="Situatie scolara")
    situatie_prof = fields.Selection([('', 'Necompletat'),
                                      ('elev', 'Elev'), ('student', 'Student'),
                                      ('salariat', 'Salariat'), ('somer', 'Somer'),
                                      ('casnic', 'Casnic'), ('independent', 'Independent'),
                                      ('ocazional', 'Lucrător ocazional'),
                                      ('agricol', 'Lucrător agricol'),
                                      ('fara', 'Fără loc de muncă')])
    dezabilitate = fields.Boolean()
    scoala = fields.Many2one('res.partner', string="Scoala", domain=[('este_scoala', '=', True)])

