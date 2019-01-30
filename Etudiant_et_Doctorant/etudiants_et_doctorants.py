from openerp import fields,models
class etudiant(models.Model):
    _name = 'etudiant'
    matricule=fields.char('matricule',size=30,required=True, help='the name')
    nom=fields.char('nom',size=30,required=True, help='the first name')
    dateN=fields.date('dateN',size=30,required=True, help='the birth date')
    prenom=fields.char('prenom',size=50, help='the email')
    id_encadreur=many2one('encadreur')
    sessionEncadrementEtudiant_ids=one2many('sessionEncadrementEtudiant','id_etudiant')

etudiant()
class doctorant(models.Model):
    _name = 'doctorant'
    nom=fields.char('first name',size=30,required=True, help='the first name')
    dateN=fields.date('date',size=30,required=True, help='the birth date')
    prenom=fields.char('email',size=50, help='the email')
    etat=fields.char('etat',size=50,help='the stat of the doctorant')
    id_encadreurD = many2one('encadreur')
    id_these=many2one('these')
    sessionEncadrementDoctorant_ids = one2many('sessionEncadrementDoctorant', 'id_doctorant')
    sessionEvaluation_ids = one2many('sessionEvaluation', 'doctorant_id')

doctorant()
class encadreur(models.Model):
    _name = 'encadreur'
    nom=fields.char('nom',size=30,required=True, help='the name')
    prenom=fields.char('prenom',size=30,required=True, help='the first name')
    dateN=fields.date('dateN',size=30,required=True, help='the birth date')
    fonction=fields.char('fonction',size=50, help='the job')
    etudiant_ids = one2many('etudiant','id_encadreur')
    doctorant_ids = one2many('doctorant', 'id_encadreurD')

encadreur()
class jury(models.Model):
    _name = 'jury'
    nom=fields.char('nom',size=30,required=True, help='the name')
    prenom=fields.char('prenom',size=30,required=True, help='the first name')
    dateN=fields.date('dateN',size=30,required=True, help='the birth date')
    fonction=fields.char('fonction',size=50, help='the job')
    sessionEvaluation_ids = one2many('sessionEvaluation','jury_id')

jury()
class these(models.Model):
    _name = 'these'
    titre=fields.char('titre',size=30,required=True, help='the title')
    description=fields.char('description',size=30,required=True, help='the description')
    doctorant_ids = one2many('doctorant','id_these')

these()
class formulaireE(models.Model):
    _name = 'formulaireE'
    note=fields.integer('note',size=30,required=True, help='the mark')
    motifs=fields.char('motifs',size=30,required=True, help='motives')
    remarques=fields.char('remarques',size=50, help='the notes')
    sessionEvaluation_id = one2many('sessionEvaluation','formulaireE_id')

formulaireE()
class sessionEvaluation(models.Model):
    _name = 'sessionEvaluation'
    heure=fields.char('titre',size=30,required=True, help='the title')
    date = fields.date('date', size=30, required=True)
    lieux = fields.char('lieux',size=30,required=True)
    doctorant_id=fields.many2one('doctorant')
    jury_id=many2one('jury')
    formulaireE_id = many2one('formulaireE')


class sessionEncadrementEtudiant(models.Model):
    _name = 'sessionEncadrement'
    heure=fields.char('titre',size=30,required=True, help='the time')
    date = fields.date('date', size=30, required=True)
    etatAvancement = fields.char('etatAvancement', size=50, help='')
    remarques = fields.char('remarques', size=50, help='the notes')
    id_etudiant=many2one('etudiant')

class sessionEncadrementDoctorant(models.Model):
    _name = 'sessionEncadrement'
    heure=fields.char('titre',size=30,required=True, help='the time')
    date = fields.date('date', size=30, required=True)
    etatAvancement = fields.char('etatAvancement', size=50, help='')
    remarques = fields.char('remarques', size=50, help='the notes')
    id_doctorant=many2one('doctorant')

