{
    'name': 'ppi',
    'author'  :'vitraining.com',
    'category': 'Human Resources',
    'description': """
Human Resource PT.PPI
""",    
    'depends': ['hr','hr_recruitment'],
    'update_xml':[
            'security/groups.xml',
            'security/ir.model.access.csv',
            'training_view.xml',
            'action.xml',
            'hr_recruitment.xml',
            'hr_applicant_view.xml',           
            'tab_training.xml',
            'ppi_workflow.xml',
            'hr_employs_tab.xml',
            ],
    'data': [],
    'installable':True,
}
