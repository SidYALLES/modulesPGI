from openerp import fields,models
class etudiant(models.Model):
    _name = 'dpgr.etudiant'
    matricule=fields.Integer('matricule',size=30,required=True, help='the name')
    nom=fields.Char('nom',size=30,required=True, help='the first name')
    dateN=fields.Date('dateN',size=30,required=True, help='the birth date')
    prenom=fields.Char('prenom',size=50, help='the email')
    id_encadreur=fields.Many2one('dpgr.encadreur')
    sessionencadrementetu_ids=fields.One2many('dpgr.sessionencadrementetu','id_etudiant')

class doctorant(models.Model):
    _name = 'dpgr.doctorant'
    nom=fields.Char('nom',size=30,required=True, help='the first name')
    dateN=fields.Date('date',size=30,required=True, help='the birth date')
    prenom=fields.Char('email',size=50, help='the email')
    etat=fields.Char('etat',size=50,help='the stat of the doctorant')
    id_encadreurD = fields.Many2one('dpgr.encadreur')
    id_these=fields.Many2one('dpgr.these')
    sessionencadrementdoc_ids = fields.One2many('dpgr.sessionencadrementdoc', 'id_doc')
    sessionevaluation_ids = fields.One2many('dpgr.sessionevaluation', 'doctorant_id')

class encadreur(models.Model):
    _name = 'dpgr.encadreur'
    nom=fields.Char('nom',size=30,required=True, help='the name')
    prenom=fields.Char('prenom',size=30,required=True, help='the first name')
    dateN=fields.Date('dateN',size=30,required=True, help='the birth date')
    fonction=fields.Char('fonction',size=50, help='the job')
    etudiant_ids = fields.One2many('dpgr.etudiant','id_encadreur')
    doctorant_ids = fields.One2many('dpgr.doctorant', 'id_encadreurD')

class jury(models.Model):
    _name = 'dpgr.jury'
    nom=fields.Char('nom',size=30,required=True, help='the name')
    prenom=fields.Char('prenom',size=30,required=True, help='the first name')
    dateN=fields.Date('dateN',size=30,required=True, help='the birth date')
    fonction=fields.Char('fonction',size=50, help='the job')
    sessionevaluation_ids = fields.One2many('dpgr.sessionevaluation','jury_id')

class these(models.Model):
    _name = 'dpgr.these'
    titre=fields.Char('titre',size=30,required=True, help='the title')
    description=fields.Char('description',size=30,required=True, help='the description')
    doctorant_ids = fields.One2many('dpgr.doctorant','id_these')

class formulaire(models.Model):
    _name = 'dpgr.formulaire'
    note=fields.Integer('note',size=30,required=True, help='the mark')
    motifs=fields.Char('motifs',size=30,required=True, help='motives')
    remarques=fields.Char('remarques',size=50, help='the notes')
    sessionevaluation_id = fields.One2many('dpgr.sessionevaluation','formulaire_id')

class sessionevaluation(models.Model):
    _name = 'dpgr.sessionevaluation'
    heure=fields.Float('titre',size=30,required=True)
    date = fields.Date('date', size=30, required=True)
    lieux = fields.Char('lieux',size=30,required=True)
    doctorant_id=fields.Many2one('dpgr.doctorant')
    jury_id=fields.Many2one('dpgr.jury')
    formulaire_id = fields.Many2one('dpgr.formulaire')


class sessionencadrementetu(models.Model):
    _name = 'dpgr.sessionencadrementetu'
    heure=fields.Char('titre',size=30,required=True, help='the time')
    date = fields.Date('date', size=30, required=True)
    etatAvancement = fields.Char('etatAvancement', size=50, help='')
    remarques = fields.Char('remarques', size=50, help='the notes')
    id_etudiant=fields.Many2one('dpgr.etudiant')

class sessionencadrementdoc(models.Model):
    _name = 'dpgr.sessionencadrementdoc'
    heure=fields.Char('titre',size=30,required=True, help='the time')
    date = fields.Date('date', size=30, required=True)
    etatAvancement = fields.Char('etatAvancement', size=50, help='')
    remarques = fields.Char('remarques', size=50, help='the notes')
    id_doc=fields.Many2one('dpgr.doctorant')


