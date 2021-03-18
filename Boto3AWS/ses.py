import boto3
ses = boto3.client('ses')

# ses.verify_email_address(
#     EmailAddress = '**************@outlook.com'
# )

#Check for verification status
print(ses.list_identities(
    IdentityType = 'EmailAddress'
) )


# #Create email template
# ses.create_template(
#     Template = {
#     'TemplateName' : 'Gabriels_Template1',
#     'SubjectPart' : 'Status update',
#     'TextPart' : 'Not a good idea ',
#     'HtmlPart': 'Thanks a lot for watching it '
# }
# )

ses.get_template(TemplateName = 'Gabriels_Template')

print(ses.list_templates())

#Send Emails

ses.send_templated_email(
    Source = '**************@outlook.com',
    Destination = {
        'ToAddresses': ['**************@outlook.com'],
        'CcAddresses': ['**************@outlook.com']

    },
    ReplyToAddresses = ['**************@outlook.com'],
    Template = 'Gabriels_Template',
    TemplateData = '{"Replace tag name":"with value"}'
)

ses.send_email(
    Source = '**************@outlook.com',
    Destination = {
        'ToAddresses': ['**************@outlook.com'],
        'CcAddresses': ['**************@outlook.com']
    },
    ReplyToAddresses=['**************@outlook.com'],
    Message = {
        'Subject' : {
            'Data': 'You can pass subject here',
            'Charset': 'utf-8'
        },
        'Body' : {
            'Text' : {
                'Data': 'Here goes your body',
                'Charset': 'utf-8'
            },
            'Html':{
                'Data':'Tis is your body message for html',
                'Charset':'utf-8'
            }

        }
    }
)
