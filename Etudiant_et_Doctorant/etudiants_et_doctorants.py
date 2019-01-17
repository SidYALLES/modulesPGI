from openerp import fields,models
class etudiant(models.Model):
    _name = 'etudiant'
    matricule=fields.char('matricule',size=30,required=True, help='the name')
    nom=fields.char('nom',size=30,required=True, help='the first name')
    dateN=fields.date('dateN',size=30,required=True, help='the birth date')
    prenom=fields.char('prenom',size=50, help='the email')
    id_encadreur=many2one('encadreur')

etudiant()
class doctorant(models.Model):
    _name = 'doctorant'
    doctorant_id=fields.integer('doctorant_id',size=30,required=True, help='the name')
    nom=fields.char('first name',size=30,required=True, help='the first name')
    dateN=fields.date('date',size=30,required=True, help='the birth date')
    prenom=fields.char('email',size=50, help='the email')
    etat=fields.char('etat',size=50,help='the stat of the doctorant')
    id_encadreurD = many2one('encadreur')
    id_these=many2one('these')

doctorant()
class encadreur(models.Model):
    _name = 'encadreur'
    nom=fields.char('nom',size=30,required=True, help='the name')
    prenom=fields.char('prenom',size=30,required=True, help='the first name')
    dateN=fields.date('dateN',size=30,required=True, help='the birth date')
    fonction=fields.char('fonction',size=50, help='the job')
    etudiant_ids = one2many('etudiant','id_encadreur')
    doctorant_ids = one2many('doctorant', 'id_encadreurD')

class these(models.Model):
    _name = 'these'
    titre=fields.char('titre',size=30,required=True, help='the title')
    description=fields.char('description',size=30,required=True, help='the description')
    doctorant_ids = one2many('doctorant','id_these')

class sessionEvaluation(models.Model):
    _name = 'sessionEvaluation'
    heure=fields.char('titre',size=30,required=True, help='the title')
    date = fields.date('date', size=30, required=True)
    lieux = fields.char('lieux',size=30,required=True)

