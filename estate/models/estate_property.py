# -*- coding: utf-8 -*-

from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Property Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char()
    date_availability = fields.Date(string='Available From', copy=False, default=fields.Date.today())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(string='Number of Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area sqm')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    gargen_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('east', 'East'),
        ('west', 'West'),
        ('south', 'South'),
    ], string='Garden Orientation', default='north')
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], string='Status', default='new', required=True)