from django.db import migrations


def populate_data(apps, schema_editor):
    Taxonomie = apps.get_model('ciel_referentiel', 'Taxonomie')
    Competence = apps.get_model('ciel_referentiel', 'Competence')
    ActiviteProfessionnelle = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelle')
    ConnaissanceAssociee = apps.get_model('ciel_referentiel', 'ConnaissanceAssociee')
    CompetenceCritereEvaluation = apps.get_model('ciel_referentiel', 'CompetenceCritereEvaluation')
    ActiviteProfessionnelleTache = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelleTache')
    ActiviteProfessionnelleMoyenRessource = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelleMoyenRessource')
    ActiviteProfessionnelleResultat = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelleResultat')

    # -------------------------------------------------------------------------
    # Taxonomie niveau 4
    # -------------------------------------------------------------------------
    Taxonomie.objects.get_or_create(
        niveau=4,
        defaults=dict(
            objectif="Maîtrise méthodologique",
            caracterisation=(
                "Maîtriser des méthodes de travail.\n"
                "Produire à partir d'éléments disparates.\n"
                "Faire des choix et les justifier."
            ),
            capacite=(
                "Coordonner des données pour concevoir une solution, un plan, un système."
            ),
            habilete="Connaissance\nCompréhension\nApplication",
            verbe=(
                "Concevoir\nConstruire\nCréer\nOrganiser\nPlanifier\n"
                "Produire\nDéduire\nÉlaborer\nFormuler\netc."
            ),
            critere_evalusation=(
                "La solution proposée est nouvelle, personnelle et adaptée à la situation."
            ),
            exemple=(
                "Proposer une méthode d'évaluation adaptée à une situation d'apprentissage."
            ),
        ),
    )

    # Raccourcis vers les taxonomies et compétences
    t1 = Taxonomie.objects.get(niveau=1)
    t2 = Taxonomie.objects.get(niveau=2)
    t3 = Taxonomie.objects.get(niveau=3)

    c04 = Competence.objects.get(code='C04')
    c06 = Competence.objects.get(code='C06')
    c07 = Competence.objects.get(code='C07')
    c08 = Competence.objects.get(code='C08')
    c09 = Competence.objects.get(code='C09')
    c10 = Competence.objects.get(code='C10')
    c11 = Competence.objects.get(code='C11')

    # -------------------------------------------------------------------------
    # Connaissances associées
    # -------------------------------------------------------------------------
    connaissances = [
        # C04 – Analyser une structure matérielle et logicielle
        (c04, t3, "Infrastructures matérielles et logicielles centralisées, décentralisées ou réparties"),
        (c04, t3, "Documents d'architecture métiers (synoptique, schéma de câblage, etc.)"),
        (c04, t2, "Acteurs de l'écosystème réglementaire et normatif et de référence des bonnes pratiques : CNIL, ANSSI / NIS, Cybermalveillance.gouv, référents informatiques de la gendarmerie nationale, etc."),
        (c04, t2, "SysML (exigences, séquence, blocs, blocs internes)"),
        (c04, t2, "Structures électroniques matérielles (analogiques et numériques)"),
        (c04, t2, "Structures programmables"),
        (c04, t3, "Programmation en langage évolué"),
        (c04, t3, "Connaissances en électronique analogique"),
        (c04, t2, "Anglais technique"),
        # C06 – Valider la conformité d'une installation
        (c06, t3, "Réseaux informatiques (protocoles, équipements et outils usuels)"),
        (c06, t1, "Principes des modèles en couches"),
        (c06, t2, "Architecture réseaux industriels et tertiaires"),
        (c06, t2, "Structures matérielles (analogiques et numériques)"),
        (c06, t2, "Structures programmables"),
        (c06, t3, "Appareils de mesure"),
        # C07 – Réaliser des maquettes et prototypes
        (c07, t3, "Technologies de boîtiers de composants (CMS, traversant, connectiques)"),
        (c07, t2, "Technologies de fabrication d'un PCB (procédés industriels)"),
        (c07, t2, "Procédés industriels de pose et brasure"),
        (c07, t3, "Procédés de prototypage"),
        (c07, t2, "Normes IPC"),
        (c07, t2, "Normes QSE"),
        (c07, t2, "Notions et concepts du développement durable appliqués aux produits électroniques et services numériques"),
        # C08 – Coder
        (c08, t2, "Langages de développement, de description, et les interfaces IDE associées"),
        (c08, t2, "Outils de modélisation"),
        (c08, t2, "Politiques internes et référentiels externes liées à la sécurisation des applications et leur environnement"),
        (c08, t2, "Infrastructures matérielles et logicielles"),
        (c08, t3, "Principes fondamentaux de programmation (variables, alternatives, boucles et fonctions)"),
        # C09 – Installer les éléments d'un système électronique ou informatique
        (c09, t3, "Plan mécanique et architectural en 2D et 3D"),
        (c09, t3, "Schémas électriques, électroniques et réseaux"),
        (c09, t3, "Technologies de raccordement : filaire, optique, fluidique etc."),
        (c09, t3, "Appareils de mesures (multimètre, oscilloscope etc.)"),
        (c09, t3, "Habilitation électrique niveau B1V"),
        (c09, t3, "Outillage mécanique et spécifique"),
        (c09, t3, "Certification AIPR (Autorisation d'Intervenir à Proximité des Réseaux)"),
        (c09, t1, "Modèles OSI/IP"),
        (c09, t3, "Protocoles usuels IPv4"),
        (c09, t3, "Éléments actifs"),
        (c09, t2, "IOT (Internet des objets)"),
        (c09, t2, "Serveur et ordinateur (Windows, Linux, virtuels, etc.)"),
        (c09, t2, "Architecture réseau et/ou système"),
        # C10 – Exploiter un réseau informatique
        (c10, t3, "Lignes de commandes d'équipements"),
        (c10, t3, "Méthodes de connexion à distance sur un équipement"),
        (c10, t2, "Système d'exploitation UNIX et Windows"),
        (c10, t2, "Les bonnes pratiques en sécurité informatique"),
        # C11 – Maintenir un système électronique ou réseau informatique
        (c11, t3, "Structures électroniques analogiques et numériques"),
        (c11, t2, "Structures programmables"),
        (c11, t2, "Caractérisation de signaux non complexes"),
        (c11, t3, "Appareils de mesure (multimètre, oscilloscope, générateurs etc.)"),
        (c11, t2, "Formation à l'habilitation électrique BR"),
        (c11, t2, "Économie de la maintenance (coûts de la maintenance)"),
        (c11, t1, "Normes QSE"),
        (c11, t2, "Différents types de maintenance"),
        (c11, t2, "Normes IPC spécifiques à la réparation"),
    ]
    for comp, taxo, conn in connaissances:
        ConnaissanceAssociee.objects.get_or_create(
            competence=comp, taxonomie=taxo, connaissance=conn
        )

    # -------------------------------------------------------------------------
    # Critères d'évaluation
    # -------------------------------------------------------------------------
    criteres = [
        # C04
        (c04, "Le besoin est identifié ainsi que les ressources matérielles, logicielles et humaines"),
        (c04, "Les logiciels d'analyse et de tests sont utilisés selon les procédures de traitement d'incidents"),
        (c04, "Les informations nécessaires sont extraites des documents réglementaires et/ou constructeurs"),
        (c04, "Les indicateurs de fonctionnement sont interprétés"),
        (c04, "Les fiches de test ou d'intervention sont renseignées"),
        (c04, "Le travail est préparé de façon à satisfaire les exigences de qualité, d'efficacité et d'échéancier"),
        (c04, "Le calme est conservé de façon constante dans des situations particulières, tout en persévérant dans la tâche jusqu'à l'atteinte du résultat sans se décourager"),
        (c04, "Les risques d'une situation de travail sont repérés et les mesures appropriées pour sa santé, sa sécurité et celle des autres sont adoptées"),
        # C06
        (c06, "Les exigences du cahier des charges sont respectées"),
        (c06, "Les tests sont effectués"),
        (c06, "Les résultats attendus sont vérifiés"),
        (c06, "La procédure de test est respectée"),
        (c06, "Le travail est effectué sans vouloir tromper, abuser, léser ou blesser les autres"),
        (c06, "Face à un ensemble de faits, des actions appropriées à poser sont décidées"),
        # C07
        (c07, "Le placement et routage sont conformes au cahier des charges"),
        (c07, "La génération des fichiers de fabrication du PCB est conforme aux attentes"),
        (c07, "Le PCB est réalisé, contrôlé et conforme aux IPC (tolérances mécaniques, finition de surface, propreté, ESD etc.)"),
        (c07, "Les composants sont conformes à la nomenclature (marquage, étiquetage)"),
        (c07, "La nomenclature des composants est respectée"),
        (c07, "Le brasage de la carte est conforme à la nomenclature et aux IPC"),
        (c07, "Les contraintes liées aux impacts environnementaux sont intégrées"),
        (c07, "Le contrôle visuel de la carte assemblée est conforme au dossier de fabrication"),
        (c07, "Les risques d'une situation de travail sont repérés et les mesures appropriées pour sa santé, sa sécurité et celle des autres sont adoptées"),
        (c07, "Le travail est effectué selon les attentes exprimées de temps, de quantité ou de qualité dans le respect des contraintes environnementales"),
        (c07, "L'effort nécessaire est fourni afin de terminer et de réussir le travail demandé"),
        (c07, "Le travail est préparé de façon à satisfaire les exigences de qualité, d'efficacité et d'échéancier"),
        # C08
        (c08, "Les environnements de développement et de test sont mis en œuvre en tenant compte des contraintes de fonctionnalités et de sécurité"),
        (c08, "Le module logiciel est débogué et syntaxiquement correct"),
        (c08, "Les composants logiciels individuels sont développés et testés conformément aux spécifications du cahier des charges et des bonnes pratiques"),
        (c08, "La solution (logicielle et matérielle) est intégrée et testée conformément aux spécifications du cahier des charges et des bonnes pratiques"),
        (c08, "Le code est commenté et le logiciel est documenté"),
        (c08, "Le travail est effectué selon les attentes exprimées de temps, de quantité ou de qualité"),
        (c08, "Le travail en équipe est conduit de manière solidaire en contribuant par des idées et des efforts"),
        # C09
        (c09, "L'ensemble des éléments pour l'installation du système est complet et vérifié par rapport au cahier des charges"),
        (c09, "Les éléments du système sont installés et raccordés selon une procédure"),
        (c09, "La configuration est réalisée"),
        (c09, "La mise en service est réalisée"),
        (c09, "L'état de l'installation est renseigné de manière écrite ou orale"),
        (c09, "Les risques d'une situation de travail sont repérés et les mesures appropriées pour sa santé, sa sécurité et celle des autres sont adoptées"),
        (c09, "Le travail est préparé de façon à satisfaire les exigences de qualité, d'efficacité et d'échéancier"),
        (c09, "Le travail est effectué selon les attentes exprimées de temps, de quantité ou de qualité"),
        (c09, "La résolution d'un problème nouveau imprévu est réussie en utilisant ses propres moyens conformément aux règles de la fonction"),
        (c09, "Des tâches diverses dans des domaines et contextes variés sont accomplies"),
        # C10
        (c10, "Les alertes et problèmes rencontrés sont renseignés"),
        (c10, "Les différents éléments d'un réseau ou d'un système à partir d'un schéma fourni sont identifiés"),
        (c10, "La mise à jour des équipements (iOS, OS, logiciel, firmware) est effectuée"),
        (c10, "Les optimisations nécessaires sont effectuées"),
        (c10, "Le travail en équipe est conduit de manière solidaire en contribuant par des idées et des efforts"),
        (c10, "Le travail est préparé de façon à satisfaire les exigences de qualité, d'efficacité et d'échéancier"),
        # C11
        (c11, "L'intervention est préparée"),
        (c11, "Le dysfonctionnement est constaté"),
        (c11, "La maintenance ou la réparation est réalisée"),
        (c11, "La fiche d'intervention est correctement renseignée"),
        (c11, "Les risques d'une situation de travail sont repérés et les mesures appropriées pour sa santé, sa sécurité et celle des autres sont adoptées"),
        (c11, "Le déroulement des tâches de travail est observé avec attention et de façon soutenue de façon à en contrôler le résultat attendu"),
        (c11, "Des idées, pratiques, ressources inhabituelles sont introduites pour l'avancement de son travail ou de celui des autres"),
    ]
    for comp, critere in criteres:
        CompetenceCritereEvaluation.objects.get_or_create(
            competence=comp, critere_evaluation=critere
        )

    # -------------------------------------------------------------------------
    # Activités R1, R2, R3, R5, D1, D2, D3 – Tâches / Moyens / Résultats
    # -------------------------------------------------------------------------
    r1 = ActiviteProfessionnelle.objects.get(code='R1')
    r2 = ActiviteProfessionnelle.objects.get(code='R2')
    r3 = ActiviteProfessionnelle.objects.get(code='R3')
    r5 = ActiviteProfessionnelle.objects.get(code='R5')
    d1 = ActiviteProfessionnelle.objects.get(code='D1')
    d2 = ActiviteProfessionnelle.objects.get(code='D2')
    d3 = ActiviteProfessionnelle.objects.get(code='D3')

    # --- Tâches (code, tache, autonomie, activite) ---
    taches = [
        # R1
        ('T1', "Prise en compte des besoins du client", 'Partielle', r1),
        ('T2', "Réception de l'installation avec le client", 'Partielle', r1),
        ('T3', "Information ou conseil au client", 'Partielle', r1),
        # R2
        ('T1', "Prise en compte de la demande du client", 'Partielle', r2),
        ('T2', "Vérification du dossier, interprétation des plans d'exécution", 'Partielle', r2),
        ('T3', "Préparation du chantier en fonction de l'intervention souhaitée", 'Partielle', r2),
        ('T4', "Réalisation des opérations avec intégration des contraintes client et contrôle", 'Partielle', r2),
        ('T5', "Recettage de l'installation", 'Partielle', r2),
        # R3
        ('T1', "Réalisation d'un diagnostic de premier niveau", 'Partielle', r3),
        ('T2', "Configuration matérielle et logicielle des équipements", 'Partielle', r3),
        ('T3', "Intégration de nouveaux équipements", 'Partielle', r3),
        ('T4', "Mise à jour des équipements", 'Partielle', r3),
        # R5
        ('T1', "Réalisation de diagnostics et d'interventions de maintenance curative", 'Partielle', r5),
        ('T2', "Réparation des liaisons, changement de cartes ou d'équipements", 'Partielle', r5),
        ('T3', "Rédaction de compte rendu d'intervention", 'Partielle', r5),
        # D1
        ('T1', "Collecte des informations", 'Partielle', d1),
        ('T2', "Analyse des informations", 'Partielle', d1),
        ('T3', "Interprétation d'un cahier des charges", 'Partielle', d1),
        ('T4', "Formalisation du cahier des charges", 'Partielle', d1),
        # D2
        ('T1', "Modélisation d'une solution logicielle", 'Partielle', d2),
        ('T2', "Développement, utilisation ou adaptation de composants logiciels", 'Partielle', d2),
        ('T3', "Tests et validation", 'Partielle', d2),
        # D3
        ('T1', "Ouvrir et catégoriser les tickets par niveau de criticité", 'Complète', d3),
        ('T2', "Traiter les tickets", 'Complète', d3),
        ('T3', "Remédier aux incidents", 'Complète', d3),
        ('T4', "Élaborer les rapports d'incidents", 'Complète', d3),
        ('T5', "Transmettre l'information (escalade)", 'Complète', d3),
    ]
    for code, tache, autonomie, activite in taches:
        ActiviteProfessionnelleTache.objects.get_or_create(
            activite_professionelle=activite,
            code=code,
            defaults=dict(tache=tache, autonomie=autonomie),
        )

    # --- Moyens et ressources ---
    moyens = [
        # R1
        (r1, "La demande d'intervention du client"),
        (r1, "Les documents contractuels"),
        (r1, "Les équipements nécessaires à la validation"),
        (r1, "Les documents et logiciels de l'entreprise"),
        (r1, "Les modalités d'intervention normalisée"),
        (r1, "La documentation mise à disposition par l'entreprise"),
        # R2
        (r2, "Le cahier des clauses techniques particulières (CCTP) et le périmètre contractuel de la demande"),
        (r2, "Les modèles documentaires nécessaires et correspondants à l'existant"),
        (r2, "Le dossier d'exécution dans son ensemble dont l'architecture réseau"),
        (r2, "Les contacts clients et prestataires, la localisation du chantier, les contraintes (matérielles, humaines, géographiques, structurelles etc.)"),
        (r2, "La liste des matériels (types et versions logiciels), les paramétrages existants"),
        (r2, "Les équipements de sécurité, d'accès au chantier, et de contrôle"),
        (r2, "La présence du client, le PV de livraison (recette)"),
        # R3
        (r3, "La documentation utilisateur"),
        (r3, "La documentation des paramétrages spécifiques des équipements opérationnels"),
        (r3, "Les documents de validation pour la nouvelle configuration, la documentation des nouveaux équipements"),
        (r3, "Le paramétrage des équipements existants"),
        # R5
        (r5, "Les outils de diagnostic"),
        (r5, "Les outils nécessaires à l'intervention"),
        (r5, "Les dossiers techniques"),
        (r5, "Les équipements de rechange"),
        (r5, "Les documents de l'entreprise"),
        # D1
        (d1, "Le dossier préliminaire du projet (expression du besoin, étude de marché etc.)"),
        (d1, "La documentation des équipements de l'entreprise (infrastructures matérielles et logicielles etc.)"),
        (d1, "Les moyens d'accès à Internet"),
        (d1, "Les outils logiciels (bureautique, modélisation, média, planification etc.)"),
        (d1, "Les contacts des intervenants sur le projet (internes, sous-traitants, client, etc.)"),
        # D2
        (d2, "Le cahier des charges"),
        (d2, "Les outils de modélisation"),
        (d2, "L'environnement de test"),
        (d2, "La documentation des équipements de l'entreprise (infrastructures matérielles et logicielles etc.)"),
        (d2, "Les infrastructures"),
        (d2, "Les logiciels de développement"),
        (d2, "Un poste de travail adapté aux besoins de développement (spécifications techniques particulières)"),
        # D3
        (d3, "Les outils logiciels (traçabilité de l'information, de tests, d'analyse et traitement de l'incident etc.)"),
        (d3, "Les documentations et procédures de traitement des incidents (support de rapport d'incidents etc.)"),
        (d3, "Les expertises et prestataires métiers (fournisseurs de services en nuage, d'équipements informatiques etc.)"),
        (d3, "L'outillage d'intervention sur les infrastructures matérielles"),
        (d3, "Les accès physiques nécessaires"),
        (d3, "Les contacts nécessaires (annuaire, liste de contacts) chez les clients et pour escalade"),
        (d3, "Les fiches réflexes de sensibilisation"),
    ]
    for activite, moyen in moyens:
        ActiviteProfessionnelleMoyenRessource.objects.get_or_create(
            activite_professionelle=activite, moyen_ressource=moyen
        )

    # --- Résultats attendus ---
    resultats = [
        # R1
        (r1, "La demande du client est prise en compte ou transférée aux services compétents"),
        (r1, "Les performances de l'installation sont validées avec le client conformément à ses prescriptions"),
        (r1, "Les documents et les données contractuels de l'installation sont remis au client"),
        (r1, "Les opérations nécessaires à la levée de réserves éventuelles sont effectuées"),
        (r1, "Le client est autonome dans la mise en œuvre de son installation"),
        (r1, "Les réponses aux questions du client sont apportées"),
        (r1, "Les informations sont transmises de manière concise et précise aux intéressés"),
        # R2
        (r2, "Les alertes sur manquements de pièces, l'interprétation des plans d'exécution face à la réalité du terrain sont effectuées"),
        (r2, "La validation des informations nécessaires et adaptées à l'intervention est effectuée sur les matériels et logiciels (types, versions etc.)"),
        (r2, "La validation des informations nécessaires et adaptées à l'intervention est effectuée sur les paramétrages existants (à réinjecter ou adapter)"),
        (r2, "La validation des informations nécessaires et adaptées à l'intervention est effectuée sur les calendaires (selon la disponibilité du client)"),
        (r2, "La validation des informations nécessaires et adaptées à l'intervention est effectuée sur les éléments environnementaux"),
        (r2, "La validation des informations nécessaires et adaptées à l'intervention est effectuée sur les états structurels et géographiques"),
        (r2, "Le cahier de recette (PV de livraison) est rempli et validé par le client"),
        (r2, "L'envoi des éventuels justificatifs de pénalités de report est effectué"),
        # R3
        (r3, "Le défaut est identifié, corrigé et la documentation est éventuellement mise à jour"),
        (r3, "Les documents de configuration sont mis à jour (matériels et logiciels)"),
        (r3, "Le cahier de recette suite à l'intégration des nouveaux équipements est complété"),
        # R5
        (r5, "La localisation de l'équipement en panne est réalisée"),
        (r5, "L'identification de la cause de défaillance est effectuée"),
        (r5, "La durée du diagnostic est optimale"),
        (r5, "Le réseau est opérationnel"),
        (r5, "Les documents sont complétés et conformes"),
        # D1
        (d1, "Le cahier des charges préliminaire est complété"),
        (d1, "Les ressources permettant de réaliser le cahier des charges sont définies"),
        (d1, "Le planning prévisionnel est établi"),
        (d1, "Les tâches sont attribuées aux divers intervenants dans le planning prévisionnel"),
        # D2
        (d2, "Les composants logiciels sont développés et testés"),
        (d2, "Les solutions logicielles sont conformes aux spécifications du cahier des charges"),
        (d2, "Le code est commenté (open source)"),
        # D3
        (d3, "L'incident est résolu dans le périmètre de ses compétences"),
        (d3, "Le rapport d'incident est établi selon les procédures de traitement de l'incident"),
        (d3, "L'incident est correctement qualifié et transmis (escalade)"),
        (d3, "Le client est correctement informé et conseillé quant aux mesures de prévention possibles"),
    ]
    for activite, resultat in resultats:
        ActiviteProfessionnelleResultat.objects.get_or_create(
            activite_professionelle=activite, resultat=resultat
        )


def reverse_populate(apps, schema_editor):
    # Suppression des données ajoutées par cette migration
    Taxonomie = apps.get_model('ciel_referentiel', 'Taxonomie')
    Competence = apps.get_model('ciel_referentiel', 'Competence')
    ActiviteProfessionnelle = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelle')
    ConnaissanceAssociee = apps.get_model('ciel_referentiel', 'ConnaissanceAssociee')
    CompetenceCritereEvaluation = apps.get_model('ciel_referentiel', 'CompetenceCritereEvaluation')
    ActiviteProfessionnelleTache = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelleTache')
    ActiviteProfessionnelleMoyenRessource = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelleMoyenRessource')
    ActiviteProfessionnelleResultat = apps.get_model('ciel_referentiel', 'ActiviteProfessionnelleResultat')

    Taxonomie.objects.filter(niveau=4).delete()

    for code in ('C04', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11'):
        comp = Competence.objects.filter(code=code).first()
        if comp:
            ConnaissanceAssociee.objects.filter(competence=comp).delete()
            CompetenceCritereEvaluation.objects.filter(competence=comp).delete()

    for code in ('R1', 'R2', 'R3', 'R5', 'D1', 'D2', 'D3'):
        act = ActiviteProfessionnelle.objects.filter(code=code).first()
        if act:
            ActiviteProfessionnelleTache.objects.filter(activite_professionelle=act).delete()
            ActiviteProfessionnelleMoyenRessource.objects.filter(activite_professionelle=act).delete()
            ActiviteProfessionnelleResultat.objects.filter(activite_professionelle=act).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('ciel_referentiel', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_populate),
    ]
