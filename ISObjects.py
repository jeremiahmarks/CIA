class ActionSequence(object):
    global actionsequences
    def __init__(self, values):
        self.values=values
        if 'actionsequences' not in globals():
            actionsequences = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'TemplateName' in values.keys():
            self.TemplateName=values['TemplateName']
        else:
            self.TemplateName=None
        if 'VisibleToTheseUsers' in values.keys():
            self.VisibleToTheseUsers=values['VisibleToTheseUsers']
        else:
            self.VisibleToTheseUsers=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.TemplateName is not None:
            vals['TemplateName'] = self.TemplateName
        if self.VisibleToTheseUsers is not None:
            vals['VisibleToTheseUsers'] = self.VisibleToTheseUsers
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TemplateName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.VisibleToTheseUsers: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class AffResource(object):
    global affresources
    def __init__(self, values):
        self.values=values
        if 'affresources' not in globals():
            affresources = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Notes' in values.keys():
            self.Notes=values['Notes']
        else:
            self.Notes=None
        if 'ProgramIds' in values.keys():
            self.ProgramIds=values['ProgramIds']
        else:
            self.ProgramIds=None
        if 'ResourceHREF' in values.keys():
            self.ResourceHREF=values['ResourceHREF']
        else:
            self.ResourceHREF=None
        if 'ResourceHTML' in values.keys():
            self.ResourceHTML=values['ResourceHTML']
        else:
            self.ResourceHTML=None
        if 'ResourceOrder' in values.keys():
            self.ResourceOrder=values['ResourceOrder']
        else:
            self.ResourceOrder=None
        if 'ResourceType' in values.keys():
            self.ResourceType=values['ResourceType']
        else:
            self.ResourceType=None
        if 'Title' in values.keys():
            self.Title=values['Title']
        else:
            self.Title=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Notes is not None:
            vals['Notes'] = self.Notes
        if self.ProgramIds is not None:
            vals['ProgramIds'] = self.ProgramIds
        if self.ResourceHREF is not None:
            vals['ResourceHREF'] = self.ResourceHREF
        if self.ResourceHTML is not None:
            vals['ResourceHTML'] = self.ResourceHTML
        if self.ResourceOrder is not None:
            vals['ResourceOrder'] = self.ResourceOrder
        if self.ResourceType is not None:
            vals['ResourceType'] = self.ResourceType
        if self.Title is not None:
            vals['Title'] = self.Title
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Notes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProgramIds: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ResourceHREF: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ResourceHTML: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ResourceOrder: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ResourceType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Affiliate(object):
    global affiliates
    def __init__(self, values):
        self.values=values
        if 'affiliates' not in globals():
            affiliates = []
        if 'AffCode' in values.keys():
            self.AffCode=values['AffCode']
        else:
            self.AffCode=None
        if 'AffName' in values.keys():
            self.AffName=values['AffName']
        else:
            self.AffName=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'DefCommissionType' in values.keys():
            self.DefCommissionType=values['DefCommissionType']
        else:
            self.DefCommissionType=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LeadAmt' in values.keys():
            self.LeadAmt=values['LeadAmt']
        else:
            self.LeadAmt=None
        if 'LeadCookieFor' in values.keys():
            self.LeadCookieFor=values['LeadCookieFor']
        else:
            self.LeadCookieFor=None
        if 'LeadPercent' in values.keys():
            self.LeadPercent=values['LeadPercent']
        else:
            self.LeadPercent=None
        if 'NotifyLead' in values.keys():
            self.NotifyLead=values['NotifyLead']
        else:
            self.NotifyLead=None
        if 'NotifySale' in values.keys():
            self.NotifySale=values['NotifySale']
        else:
            self.NotifySale=None
        if 'ParentId' in values.keys():
            self.ParentId=values['ParentId']
        else:
            self.ParentId=None
        if 'Password' in values.keys():
            self.Password=values['Password']
        else:
            self.Password=None
        if 'PayoutType' in values.keys():
            self.PayoutType=values['PayoutType']
        else:
            self.PayoutType=None
        if 'SaleAmt' in values.keys():
            self.SaleAmt=values['SaleAmt']
        else:
            self.SaleAmt=None
        if 'SalePercent' in values.keys():
            self.SalePercent=values['SalePercent']
        else:
            self.SalePercent=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None

    def prepare(self):
        vals={}
        if self.AffCode is not None:
            vals['AffCode'] = self.AffCode
        if self.AffName is not None:
            vals['AffName'] = self.AffName
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.DefCommissionType is not None:
            vals['DefCommissionType'] = self.DefCommissionType
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LeadAmt is not None:
            vals['LeadAmt'] = self.LeadAmt
        if self.LeadCookieFor is not None:
            vals['LeadCookieFor'] = self.LeadCookieFor
        if self.LeadPercent is not None:
            vals['LeadPercent'] = self.LeadPercent
        if self.NotifyLead is not None:
            vals['NotifyLead'] = self.NotifyLead
        if self.NotifySale is not None:
            vals['NotifySale'] = self.NotifySale
        if self.ParentId is not None:
            vals['ParentId'] = self.ParentId
        if self.Password is not None:
            vals['Password'] = self.Password
        if self.PayoutType is not None:
            vals['PayoutType'] = self.PayoutType
        if self.SaleAmt is not None:
            vals['SaleAmt'] = self.SaleAmt
        if self.SalePercent is not None:
            vals['SalePercent'] = self.SalePercent
        if self.Status is not None:
            vals['Status'] = self.Status
        return vals

    def _template(self):
        if self.AffCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AffName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DefCommissionType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadCookieFor: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadPercent: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NotifyLead: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NotifySale: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ParentId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Password: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayoutType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SaleAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SalePercent: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class CCharge(object):
    global ccharges
    def __init__(self, values):
        self.values=values
        if 'ccharges' not in globals():
            ccharges = []
        if 'Amt' in values.keys():
            self.Amt=values['Amt']
        else:
            self.Amt=None
        if 'ApprCode' in values.keys():
            self.ApprCode=values['ApprCode']
        else:
            self.ApprCode=None
        if 'CCId' in values.keys():
            self.CCId=values['CCId']
        else:
            self.CCId=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'MerchantId' in values.keys():
            self.MerchantId=values['MerchantId']
        else:
            self.MerchantId=None
        if 'OrderNum' in values.keys():
            self.OrderNum=values['OrderNum']
        else:
            self.OrderNum=None
        if 'PaymentId' in values.keys():
            self.PaymentId=values['PaymentId']
        else:
            self.PaymentId=None
        if 'RefNum' in values.keys():
            self.RefNum=values['RefNum']
        else:
            self.RefNum=None

    def prepare(self):
        vals={}
        if self.Amt is not None:
            vals['Amt'] = self.Amt
        if self.ApprCode is not None:
            vals['ApprCode'] = self.ApprCode
        if self.CCId is not None:
            vals['CCId'] = self.CCId
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.MerchantId is not None:
            vals['MerchantId'] = self.MerchantId
        if self.OrderNum is not None:
            vals['OrderNum'] = self.OrderNum
        if self.PaymentId is not None:
            vals['PaymentId'] = self.PaymentId
        if self.RefNum is not None:
            vals['RefNum'] = self.RefNum
        return vals

    def _template(self):
        if self.Amt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ApprCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CCId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MerchantId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OrderNum: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PaymentId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.RefNum: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class CProgram(object):
    global cprograms
    def __init__(self, values):
        self.values=values
        if 'cprograms' not in globals():
            cprograms = []
        if 'Active' in values.keys():
            self.Active=values['Active']
        else:
            self.Active=None
        if 'BillingType' in values.keys():
            self.BillingType=values['BillingType']
        else:
            self.BillingType=None
        if 'DefaultCycle' in values.keys():
            self.DefaultCycle=values['DefaultCycle']
        else:
            self.DefaultCycle=None
        if 'DefaultFrequency' in values.keys():
            self.DefaultFrequency=values['DefaultFrequency']
        else:
            self.DefaultFrequency=None
        if 'DefaultPrice' in values.keys():
            self.DefaultPrice=values['DefaultPrice']
        else:
            self.DefaultPrice=None
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'Family' in values.keys():
            self.Family=values['Family']
        else:
            self.Family=None
        if 'HideInStore' in values.keys():
            self.HideInStore=values['HideInStore']
        else:
            self.HideInStore=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LargeImage' in values.keys():
            self.LargeImage=values['LargeImage']
        else:
            self.LargeImage=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'ProgramName' in values.keys():
            self.ProgramName=values['ProgramName']
        else:
            self.ProgramName=None
        if 'ShortDescription' in values.keys():
            self.ShortDescription=values['ShortDescription']
        else:
            self.ShortDescription=None
        if 'Sku' in values.keys():
            self.Sku=values['Sku']
        else:
            self.Sku=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None
        if 'Taxable' in values.keys():
            self.Taxable=values['Taxable']
        else:
            self.Taxable=None

    def prepare(self):
        vals={}
        if self.Active is not None:
            vals['Active'] = self.Active
        if self.BillingType is not None:
            vals['BillingType'] = self.BillingType
        if self.DefaultCycle is not None:
            vals['DefaultCycle'] = self.DefaultCycle
        if self.DefaultFrequency is not None:
            vals['DefaultFrequency'] = self.DefaultFrequency
        if self.DefaultPrice is not None:
            vals['DefaultPrice'] = self.DefaultPrice
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.Family is not None:
            vals['Family'] = self.Family
        if self.HideInStore is not None:
            vals['HideInStore'] = self.HideInStore
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LargeImage is not None:
            vals['LargeImage'] = self.LargeImage
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.ProgramName is not None:
            vals['ProgramName'] = self.ProgramName
        if self.ShortDescription is not None:
            vals['ShortDescription'] = self.ShortDescription
        if self.Sku is not None:
            vals['Sku'] = self.Sku
        if self.Status is not None:
            vals['Status'] = self.Status
        if self.Taxable is not None:
            vals['Taxable'] = self.Taxable
        return vals

    def _template(self):
        if self.Active: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillingType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DefaultCycle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DefaultFrequency: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DefaultPrice: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Family: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.HideInStore: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LargeImage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProgramName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShortDescription: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Sku: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Taxable: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Campaign(object):
    global campaigns
    def __init__(self, values):
        self.values=values
        if 'campaigns' not in globals():
            campaigns = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Name is not None:
            vals['Name'] = self.Name
        if self.Status is not None:
            vals['Status'] = self.Status
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class CampaignStep(object):
    global campaignsteps
    def __init__(self, values):
        self.values=values
        if 'campaignsteps' not in globals():
            campaignsteps = []
        if 'CampaignId' in values.keys():
            self.CampaignId=values['CampaignId']
        else:
            self.CampaignId=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'StepStatus' in values.keys():
            self.StepStatus=values['StepStatus']
        else:
            self.StepStatus=None
        if 'StepTitle' in values.keys():
            self.StepTitle=values['StepTitle']
        else:
            self.StepTitle=None
        if 'TemplateId' in values.keys():
            self.TemplateId=values['TemplateId']
        else:
            self.TemplateId=None

    def prepare(self):
        vals={}
        if self.CampaignId is not None:
            vals['CampaignId'] = self.CampaignId
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.StepStatus is not None:
            vals['StepStatus'] = self.StepStatus
        if self.StepTitle is not None:
            vals['StepTitle'] = self.StepTitle
        if self.TemplateId is not None:
            vals['TemplateId'] = self.TemplateId
        return vals

    def _template(self):
        if self.CampaignId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StepStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StepTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TemplateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Campaignee(object):
    global campaignees
    def __init__(self, values):
        self.values=values
        if 'campaignees' not in globals():
            campaignees = []
        if 'Campaign' in values.keys():
            self.Campaign=values['Campaign']
        else:
            self.Campaign=None
        if 'CampaignId' in values.keys():
            self.CampaignId=values['CampaignId']
        else:
            self.CampaignId=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None

    def prepare(self):
        vals={}
        if self.Campaign is not None:
            vals['Campaign'] = self.Campaign
        if self.CampaignId is not None:
            vals['CampaignId'] = self.CampaignId
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.Status is not None:
            vals['Status'] = self.Status
        return vals

    def _template(self):
        if self.Campaign: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CampaignId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Company(object):
    global companys
    def __init__(self, values):
        self.values=values
        if 'companys' not in globals():
            companys = []
        if 'AccountId' in values.keys():
            self.AccountId=values['AccountId']
        else:
            self.AccountId=None
        if 'Address1Type' in values.keys():
            self.Address1Type=values['Address1Type']
        else:
            self.Address1Type=None
        if 'Address2Street1' in values.keys():
            self.Address2Street1=values['Address2Street1']
        else:
            self.Address2Street1=None
        if 'Address2Street2' in values.keys():
            self.Address2Street2=values['Address2Street2']
        else:
            self.Address2Street2=None
        if 'Address2Type' in values.keys():
            self.Address2Type=values['Address2Type']
        else:
            self.Address2Type=None
        if 'Address3Street1' in values.keys():
            self.Address3Street1=values['Address3Street1']
        else:
            self.Address3Street1=None
        if 'Address3Street2' in values.keys():
            self.Address3Street2=values['Address3Street2']
        else:
            self.Address3Street2=None
        if 'Address3Type' in values.keys():
            self.Address3Type=values['Address3Type']
        else:
            self.Address3Type=None
        if 'Anniversary' in values.keys():
            self.Anniversary=values['Anniversary']
        else:
            self.Anniversary=None
        if 'AssistantName' in values.keys():
            self.AssistantName=values['AssistantName']
        else:
            self.AssistantName=None
        if 'AssistantPhone' in values.keys():
            self.AssistantPhone=values['AssistantPhone']
        else:
            self.AssistantPhone=None
        if 'BillingInformation' in values.keys():
            self.BillingInformation=values['BillingInformation']
        else:
            self.BillingInformation=None
        if 'Birthday' in values.keys():
            self.Birthday=values['Birthday']
        else:
            self.Birthday=None
        if 'City' in values.keys():
            self.City=values['City']
        else:
            self.City=None
        if 'City2' in values.keys():
            self.City2=values['City2']
        else:
            self.City2=None
        if 'City3' in values.keys():
            self.City3=values['City3']
        else:
            self.City3=None
        if 'Company' in values.keys():
            self.Company=values['Company']
        else:
            self.Company=None
        if 'CompanyID' in values.keys():
            self.CompanyID=values['CompanyID']
        else:
            self.CompanyID=None
        if 'ContactNotes' in values.keys():
            self.ContactNotes=values['ContactNotes']
        else:
            self.ContactNotes=None
        if 'ContactType' in values.keys():
            self.ContactType=values['ContactType']
        else:
            self.ContactType=None
        if 'Country' in values.keys():
            self.Country=values['Country']
        else:
            self.Country=None
        if 'Country2' in values.keys():
            self.Country2=values['Country2']
        else:
            self.Country2=None
        if 'Country3' in values.keys():
            self.Country3=values['Country3']
        else:
            self.Country3=None
        if 'CreatedBy' in values.keys():
            self.CreatedBy=values['CreatedBy']
        else:
            self.CreatedBy=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'Email' in values.keys():
            self.Email=values['Email']
        else:
            self.Email=None
        if 'EmailAddress2' in values.keys():
            self.EmailAddress2=values['EmailAddress2']
        else:
            self.EmailAddress2=None
        if 'EmailAddress3' in values.keys():
            self.EmailAddress3=values['EmailAddress3']
        else:
            self.EmailAddress3=None
        if 'Fax1' in values.keys():
            self.Fax1=values['Fax1']
        else:
            self.Fax1=None
        if 'Fax1Type' in values.keys():
            self.Fax1Type=values['Fax1Type']
        else:
            self.Fax1Type=None
        if 'Fax2' in values.keys():
            self.Fax2=values['Fax2']
        else:
            self.Fax2=None
        if 'Fax2Type' in values.keys():
            self.Fax2Type=values['Fax2Type']
        else:
            self.Fax2Type=None
        if 'FirstName' in values.keys():
            self.FirstName=values['FirstName']
        else:
            self.FirstName=None
        if 'Groups' in values.keys():
            self.Groups=values['Groups']
        else:
            self.Groups=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'JobTitle' in values.keys():
            self.JobTitle=values['JobTitle']
        else:
            self.JobTitle=None
        if 'LastName' in values.keys():
            self.LastName=values['LastName']
        else:
            self.LastName=None
        if 'LastUpdated' in values.keys():
            self.LastUpdated=values['LastUpdated']
        else:
            self.LastUpdated=None
        if 'LastUpdatedBy' in values.keys():
            self.LastUpdatedBy=values['LastUpdatedBy']
        else:
            self.LastUpdatedBy=None
        if 'MiddleName' in values.keys():
            self.MiddleName=values['MiddleName']
        else:
            self.MiddleName=None
        if 'Nickname' in values.keys():
            self.Nickname=values['Nickname']
        else:
            self.Nickname=None
        if 'OwnerID' in values.keys():
            self.OwnerID=values['OwnerID']
        else:
            self.OwnerID=None
        if 'Password' in values.keys():
            self.Password=values['Password']
        else:
            self.Password=None
        if 'Phone1' in values.keys():
            self.Phone1=values['Phone1']
        else:
            self.Phone1=None
        if 'Phone1Ext' in values.keys():
            self.Phone1Ext=values['Phone1Ext']
        else:
            self.Phone1Ext=None
        if 'Phone1Type' in values.keys():
            self.Phone1Type=values['Phone1Type']
        else:
            self.Phone1Type=None
        if 'Phone2' in values.keys():
            self.Phone2=values['Phone2']
        else:
            self.Phone2=None
        if 'Phone2Ext' in values.keys():
            self.Phone2Ext=values['Phone2Ext']
        else:
            self.Phone2Ext=None
        if 'Phone2Type' in values.keys():
            self.Phone2Type=values['Phone2Type']
        else:
            self.Phone2Type=None
        if 'Phone3' in values.keys():
            self.Phone3=values['Phone3']
        else:
            self.Phone3=None
        if 'Phone3Ext' in values.keys():
            self.Phone3Ext=values['Phone3Ext']
        else:
            self.Phone3Ext=None
        if 'Phone3Type' in values.keys():
            self.Phone3Type=values['Phone3Type']
        else:
            self.Phone3Type=None
        if 'Phone4' in values.keys():
            self.Phone4=values['Phone4']
        else:
            self.Phone4=None
        if 'Phone4Ext' in values.keys():
            self.Phone4Ext=values['Phone4Ext']
        else:
            self.Phone4Ext=None
        if 'Phone4Type' in values.keys():
            self.Phone4Type=values['Phone4Type']
        else:
            self.Phone4Type=None
        if 'Phone5' in values.keys():
            self.Phone5=values['Phone5']
        else:
            self.Phone5=None
        if 'Phone5Ext' in values.keys():
            self.Phone5Ext=values['Phone5Ext']
        else:
            self.Phone5Ext=None
        if 'Phone5Type' in values.keys():
            self.Phone5Type=values['Phone5Type']
        else:
            self.Phone5Type=None
        if 'PostalCode' in values.keys():
            self.PostalCode=values['PostalCode']
        else:
            self.PostalCode=None
        if 'PostalCode2' in values.keys():
            self.PostalCode2=values['PostalCode2']
        else:
            self.PostalCode2=None
        if 'PostalCode3' in values.keys():
            self.PostalCode3=values['PostalCode3']
        else:
            self.PostalCode3=None
        if 'ReferralCode' in values.keys():
            self.ReferralCode=values['ReferralCode']
        else:
            self.ReferralCode=None
        if 'SpouseName' in values.keys():
            self.SpouseName=values['SpouseName']
        else:
            self.SpouseName=None
        if 'State' in values.keys():
            self.State=values['State']
        else:
            self.State=None
        if 'State2' in values.keys():
            self.State2=values['State2']
        else:
            self.State2=None
        if 'State3' in values.keys():
            self.State3=values['State3']
        else:
            self.State3=None
        if 'StreetAddress1' in values.keys():
            self.StreetAddress1=values['StreetAddress1']
        else:
            self.StreetAddress1=None
        if 'StreetAddress2' in values.keys():
            self.StreetAddress2=values['StreetAddress2']
        else:
            self.StreetAddress2=None
        if 'Suffix' in values.keys():
            self.Suffix=values['Suffix']
        else:
            self.Suffix=None
        if 'Title' in values.keys():
            self.Title=values['Title']
        else:
            self.Title=None
        if 'Username' in values.keys():
            self.Username=values['Username']
        else:
            self.Username=None
        if 'Validated' in values.keys():
            self.Validated=values['Validated']
        else:
            self.Validated=None
        if 'Website' in values.keys():
            self.Website=values['Website']
        else:
            self.Website=None
        if 'ZipFour1' in values.keys():
            self.ZipFour1=values['ZipFour1']
        else:
            self.ZipFour1=None
        if 'ZipFour2' in values.keys():
            self.ZipFour2=values['ZipFour2']
        else:
            self.ZipFour2=None
        if 'ZipFour3' in values.keys():
            self.ZipFour3=values['ZipFour3']
        else:
            self.ZipFour3=None

    def prepare(self):
        vals={}
        if self.AccountId is not None:
            vals['AccountId'] = self.AccountId
        if self.Address1Type is not None:
            vals['Address1Type'] = self.Address1Type
        if self.Address2Street1 is not None:
            vals['Address2Street1'] = self.Address2Street1
        if self.Address2Street2 is not None:
            vals['Address2Street2'] = self.Address2Street2
        if self.Address2Type is not None:
            vals['Address2Type'] = self.Address2Type
        if self.Address3Street1 is not None:
            vals['Address3Street1'] = self.Address3Street1
        if self.Address3Street2 is not None:
            vals['Address3Street2'] = self.Address3Street2
        if self.Address3Type is not None:
            vals['Address3Type'] = self.Address3Type
        if self.Anniversary is not None:
            vals['Anniversary'] = self.Anniversary
        if self.AssistantName is not None:
            vals['AssistantName'] = self.AssistantName
        if self.AssistantPhone is not None:
            vals['AssistantPhone'] = self.AssistantPhone
        if self.BillingInformation is not None:
            vals['BillingInformation'] = self.BillingInformation
        if self.Birthday is not None:
            vals['Birthday'] = self.Birthday
        if self.City is not None:
            vals['City'] = self.City
        if self.City2 is not None:
            vals['City2'] = self.City2
        if self.City3 is not None:
            vals['City3'] = self.City3
        if self.Company is not None:
            vals['Company'] = self.Company
        if self.CompanyID is not None:
            vals['CompanyID'] = self.CompanyID
        if self.ContactNotes is not None:
            vals['ContactNotes'] = self.ContactNotes
        if self.ContactType is not None:
            vals['ContactType'] = self.ContactType
        if self.Country is not None:
            vals['Country'] = self.Country
        if self.Country2 is not None:
            vals['Country2'] = self.Country2
        if self.Country3 is not None:
            vals['Country3'] = self.Country3
        if self.CreatedBy is not None:
            vals['CreatedBy'] = self.CreatedBy
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.Email is not None:
            vals['Email'] = self.Email
        if self.EmailAddress2 is not None:
            vals['EmailAddress2'] = self.EmailAddress2
        if self.EmailAddress3 is not None:
            vals['EmailAddress3'] = self.EmailAddress3
        if self.Fax1 is not None:
            vals['Fax1'] = self.Fax1
        if self.Fax1Type is not None:
            vals['Fax1Type'] = self.Fax1Type
        if self.Fax2 is not None:
            vals['Fax2'] = self.Fax2
        if self.Fax2Type is not None:
            vals['Fax2Type'] = self.Fax2Type
        if self.FirstName is not None:
            vals['FirstName'] = self.FirstName
        if self.Groups is not None:
            vals['Groups'] = self.Groups
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.JobTitle is not None:
            vals['JobTitle'] = self.JobTitle
        if self.LastName is not None:
            vals['LastName'] = self.LastName
        if self.LastUpdated is not None:
            vals['LastUpdated'] = self.LastUpdated
        if self.LastUpdatedBy is not None:
            vals['LastUpdatedBy'] = self.LastUpdatedBy
        if self.MiddleName is not None:
            vals['MiddleName'] = self.MiddleName
        if self.Nickname is not None:
            vals['Nickname'] = self.Nickname
        if self.OwnerID is not None:
            vals['OwnerID'] = self.OwnerID
        if self.Password is not None:
            vals['Password'] = self.Password
        if self.Phone1 is not None:
            vals['Phone1'] = self.Phone1
        if self.Phone1Ext is not None:
            vals['Phone1Ext'] = self.Phone1Ext
        if self.Phone1Type is not None:
            vals['Phone1Type'] = self.Phone1Type
        if self.Phone2 is not None:
            vals['Phone2'] = self.Phone2
        if self.Phone2Ext is not None:
            vals['Phone2Ext'] = self.Phone2Ext
        if self.Phone2Type is not None:
            vals['Phone2Type'] = self.Phone2Type
        if self.Phone3 is not None:
            vals['Phone3'] = self.Phone3
        if self.Phone3Ext is not None:
            vals['Phone3Ext'] = self.Phone3Ext
        if self.Phone3Type is not None:
            vals['Phone3Type'] = self.Phone3Type
        if self.Phone4 is not None:
            vals['Phone4'] = self.Phone4
        if self.Phone4Ext is not None:
            vals['Phone4Ext'] = self.Phone4Ext
        if self.Phone4Type is not None:
            vals['Phone4Type'] = self.Phone4Type
        if self.Phone5 is not None:
            vals['Phone5'] = self.Phone5
        if self.Phone5Ext is not None:
            vals['Phone5Ext'] = self.Phone5Ext
        if self.Phone5Type is not None:
            vals['Phone5Type'] = self.Phone5Type
        if self.PostalCode is not None:
            vals['PostalCode'] = self.PostalCode
        if self.PostalCode2 is not None:
            vals['PostalCode2'] = self.PostalCode2
        if self.PostalCode3 is not None:
            vals['PostalCode3'] = self.PostalCode3
        if self.ReferralCode is not None:
            vals['ReferralCode'] = self.ReferralCode
        if self.SpouseName is not None:
            vals['SpouseName'] = self.SpouseName
        if self.State is not None:
            vals['State'] = self.State
        if self.State2 is not None:
            vals['State2'] = self.State2
        if self.State3 is not None:
            vals['State3'] = self.State3
        if self.StreetAddress1 is not None:
            vals['StreetAddress1'] = self.StreetAddress1
        if self.StreetAddress2 is not None:
            vals['StreetAddress2'] = self.StreetAddress2
        if self.Suffix is not None:
            vals['Suffix'] = self.Suffix
        if self.Title is not None:
            vals['Title'] = self.Title
        if self.Username is not None:
            vals['Username'] = self.Username
        if self.Validated is not None:
            vals['Validated'] = self.Validated
        if self.Website is not None:
            vals['Website'] = self.Website
        if self.ZipFour1 is not None:
            vals['ZipFour1'] = self.ZipFour1
        if self.ZipFour2 is not None:
            vals['ZipFour2'] = self.ZipFour2
        if self.ZipFour3 is not None:
            vals['ZipFour3'] = self.ZipFour3
        return vals

    def _template(self):
        if self.AccountId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address2Street1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address2Street2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address3Street1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address3Street2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address3Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Anniversary: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AssistantName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AssistantPhone: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillingInformation: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Birthday: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.City: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.City2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.City3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Company: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CompanyID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactNotes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Country: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Country2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Country3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Email: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Groups: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.JobTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MiddleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Nickname: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OwnerID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Password: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone3Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone3Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone4: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone4Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone4Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone5: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone5Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone5Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ReferralCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SpouseName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Suffix: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Username: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Validated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Website: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour3: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Contact(object):
    global contacts
    def __init__(self, values):
        self.values=values
        if 'contacts' not in globals():
            contacts = []
        if 'AccountId' in values.keys():
            self.AccountId=values['AccountId']
        else:
            self.AccountId=None
        if 'Address1Type' in values.keys():
            self.Address1Type=values['Address1Type']
        else:
            self.Address1Type=None
        if 'Address2Street1' in values.keys():
            self.Address2Street1=values['Address2Street1']
        else:
            self.Address2Street1=None
        if 'Address2Street2' in values.keys():
            self.Address2Street2=values['Address2Street2']
        else:
            self.Address2Street2=None
        if 'Address2Type' in values.keys():
            self.Address2Type=values['Address2Type']
        else:
            self.Address2Type=None
        if 'Address3Street1' in values.keys():
            self.Address3Street1=values['Address3Street1']
        else:
            self.Address3Street1=None
        if 'Address3Street2' in values.keys():
            self.Address3Street2=values['Address3Street2']
        else:
            self.Address3Street2=None
        if 'Address3Type' in values.keys():
            self.Address3Type=values['Address3Type']
        else:
            self.Address3Type=None
        if 'Anniversary' in values.keys():
            self.Anniversary=values['Anniversary']
        else:
            self.Anniversary=None
        if 'AssistantName' in values.keys():
            self.AssistantName=values['AssistantName']
        else:
            self.AssistantName=None
        if 'AssistantPhone' in values.keys():
            self.AssistantPhone=values['AssistantPhone']
        else:
            self.AssistantPhone=None
        if 'BillingInformation' in values.keys():
            self.BillingInformation=values['BillingInformation']
        else:
            self.BillingInformation=None
        if 'Birthday' in values.keys():
            self.Birthday=values['Birthday']
        else:
            self.Birthday=None
        if 'City' in values.keys():
            self.City=values['City']
        else:
            self.City=None
        if 'City2' in values.keys():
            self.City2=values['City2']
        else:
            self.City2=None
        if 'City3' in values.keys():
            self.City3=values['City3']
        else:
            self.City3=None
        if 'Company' in values.keys():
            self.Company=values['Company']
        else:
            self.Company=None
        if 'CompanyID' in values.keys():
            self.CompanyID=values['CompanyID']
        else:
            self.CompanyID=None
        if 'ContactNotes' in values.keys():
            self.ContactNotes=values['ContactNotes']
        else:
            self.ContactNotes=None
        if 'ContactType' in values.keys():
            self.ContactType=values['ContactType']
        else:
            self.ContactType=None
        if 'Country' in values.keys():
            self.Country=values['Country']
        else:
            self.Country=None
        if 'Country2' in values.keys():
            self.Country2=values['Country2']
        else:
            self.Country2=None
        if 'Country3' in values.keys():
            self.Country3=values['Country3']
        else:
            self.Country3=None
        if 'CreatedBy' in values.keys():
            self.CreatedBy=values['CreatedBy']
        else:
            self.CreatedBy=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'Email' in values.keys():
            self.Email=values['Email']
        else:
            self.Email=None
        if 'EmailAddress2' in values.keys():
            self.EmailAddress2=values['EmailAddress2']
        else:
            self.EmailAddress2=None
        if 'EmailAddress3' in values.keys():
            self.EmailAddress3=values['EmailAddress3']
        else:
            self.EmailAddress3=None
        if 'Fax1' in values.keys():
            self.Fax1=values['Fax1']
        else:
            self.Fax1=None
        if 'Fax1Type' in values.keys():
            self.Fax1Type=values['Fax1Type']
        else:
            self.Fax1Type=None
        if 'Fax2' in values.keys():
            self.Fax2=values['Fax2']
        else:
            self.Fax2=None
        if 'Fax2Type' in values.keys():
            self.Fax2Type=values['Fax2Type']
        else:
            self.Fax2Type=None
        if 'FirstName' in values.keys():
            self.FirstName=values['FirstName']
        else:
            self.FirstName=None
        if 'Groups' in values.keys():
            self.Groups=values['Groups']
        else:
            self.Groups=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'JobTitle' in values.keys():
            self.JobTitle=values['JobTitle']
        else:
            self.JobTitle=None
        if 'LastName' in values.keys():
            self.LastName=values['LastName']
        else:
            self.LastName=None
        if 'LastUpdated' in values.keys():
            self.LastUpdated=values['LastUpdated']
        else:
            self.LastUpdated=None
        if 'LastUpdatedBy' in values.keys():
            self.LastUpdatedBy=values['LastUpdatedBy']
        else:
            self.LastUpdatedBy=None
        if 'LeadSourceId' in values.keys():
            self.LeadSourceId=values['LeadSourceId']
        else:
            self.LeadSourceId=None
        if 'Leadsource' in values.keys():
            self.Leadsource=values['Leadsource']
        else:
            self.Leadsource=None
        if 'MiddleName' in values.keys():
            self.MiddleName=values['MiddleName']
        else:
            self.MiddleName=None
        if 'Nickname' in values.keys():
            self.Nickname=values['Nickname']
        else:
            self.Nickname=None
        if 'OwnerID' in values.keys():
            self.OwnerID=values['OwnerID']
        else:
            self.OwnerID=None
        if 'Password' in values.keys():
            self.Password=values['Password']
        else:
            self.Password=None
        if 'Phone1' in values.keys():
            self.Phone1=values['Phone1']
        else:
            self.Phone1=None
        if 'Phone1Ext' in values.keys():
            self.Phone1Ext=values['Phone1Ext']
        else:
            self.Phone1Ext=None
        if 'Phone1Type' in values.keys():
            self.Phone1Type=values['Phone1Type']
        else:
            self.Phone1Type=None
        if 'Phone2' in values.keys():
            self.Phone2=values['Phone2']
        else:
            self.Phone2=None
        if 'Phone2Ext' in values.keys():
            self.Phone2Ext=values['Phone2Ext']
        else:
            self.Phone2Ext=None
        if 'Phone2Type' in values.keys():
            self.Phone2Type=values['Phone2Type']
        else:
            self.Phone2Type=None
        if 'Phone3' in values.keys():
            self.Phone3=values['Phone3']
        else:
            self.Phone3=None
        if 'Phone3Ext' in values.keys():
            self.Phone3Ext=values['Phone3Ext']
        else:
            self.Phone3Ext=None
        if 'Phone3Type' in values.keys():
            self.Phone3Type=values['Phone3Type']
        else:
            self.Phone3Type=None
        if 'Phone4' in values.keys():
            self.Phone4=values['Phone4']
        else:
            self.Phone4=None
        if 'Phone4Ext' in values.keys():
            self.Phone4Ext=values['Phone4Ext']
        else:
            self.Phone4Ext=None
        if 'Phone4Type' in values.keys():
            self.Phone4Type=values['Phone4Type']
        else:
            self.Phone4Type=None
        if 'Phone5' in values.keys():
            self.Phone5=values['Phone5']
        else:
            self.Phone5=None
        if 'Phone5Ext' in values.keys():
            self.Phone5Ext=values['Phone5Ext']
        else:
            self.Phone5Ext=None
        if 'Phone5Type' in values.keys():
            self.Phone5Type=values['Phone5Type']
        else:
            self.Phone5Type=None
        if 'PostalCode' in values.keys():
            self.PostalCode=values['PostalCode']
        else:
            self.PostalCode=None
        if 'PostalCode2' in values.keys():
            self.PostalCode2=values['PostalCode2']
        else:
            self.PostalCode2=None
        if 'PostalCode3' in values.keys():
            self.PostalCode3=values['PostalCode3']
        else:
            self.PostalCode3=None
        if 'ReferralCode' in values.keys():
            self.ReferralCode=values['ReferralCode']
        else:
            self.ReferralCode=None
        if 'SpouseName' in values.keys():
            self.SpouseName=values['SpouseName']
        else:
            self.SpouseName=None
        if 'State' in values.keys():
            self.State=values['State']
        else:
            self.State=None
        if 'State2' in values.keys():
            self.State2=values['State2']
        else:
            self.State2=None
        if 'State3' in values.keys():
            self.State3=values['State3']
        else:
            self.State3=None
        if 'StreetAddress1' in values.keys():
            self.StreetAddress1=values['StreetAddress1']
        else:
            self.StreetAddress1=None
        if 'StreetAddress2' in values.keys():
            self.StreetAddress2=values['StreetAddress2']
        else:
            self.StreetAddress2=None
        if 'Suffix' in values.keys():
            self.Suffix=values['Suffix']
        else:
            self.Suffix=None
        if 'Title' in values.keys():
            self.Title=values['Title']
        else:
            self.Title=None
        if 'Username' in values.keys():
            self.Username=values['Username']
        else:
            self.Username=None
        if 'Validated' in values.keys():
            self.Validated=values['Validated']
        else:
            self.Validated=None
        if 'Website' in values.keys():
            self.Website=values['Website']
        else:
            self.Website=None
        if 'ZipFour1' in values.keys():
            self.ZipFour1=values['ZipFour1']
        else:
            self.ZipFour1=None
        if 'ZipFour2' in values.keys():
            self.ZipFour2=values['ZipFour2']
        else:
            self.ZipFour2=None
        if 'ZipFour3' in values.keys():
            self.ZipFour3=values['ZipFour3']
        else:
            self.ZipFour3=None

    def prepare(self):
        vals={}
        if self.AccountId is not None:
            vals['AccountId'] = self.AccountId
        if self.Address1Type is not None:
            vals['Address1Type'] = self.Address1Type
        if self.Address2Street1 is not None:
            vals['Address2Street1'] = self.Address2Street1
        if self.Address2Street2 is not None:
            vals['Address2Street2'] = self.Address2Street2
        if self.Address2Type is not None:
            vals['Address2Type'] = self.Address2Type
        if self.Address3Street1 is not None:
            vals['Address3Street1'] = self.Address3Street1
        if self.Address3Street2 is not None:
            vals['Address3Street2'] = self.Address3Street2
        if self.Address3Type is not None:
            vals['Address3Type'] = self.Address3Type
        if self.Anniversary is not None:
            vals['Anniversary'] = self.Anniversary
        if self.AssistantName is not None:
            vals['AssistantName'] = self.AssistantName
        if self.AssistantPhone is not None:
            vals['AssistantPhone'] = self.AssistantPhone
        if self.BillingInformation is not None:
            vals['BillingInformation'] = self.BillingInformation
        if self.Birthday is not None:
            vals['Birthday'] = self.Birthday
        if self.City is not None:
            vals['City'] = self.City
        if self.City2 is not None:
            vals['City2'] = self.City2
        if self.City3 is not None:
            vals['City3'] = self.City3
        if self.Company is not None:
            vals['Company'] = self.Company
        if self.CompanyID is not None:
            vals['CompanyID'] = self.CompanyID
        if self.ContactNotes is not None:
            vals['ContactNotes'] = self.ContactNotes
        if self.ContactType is not None:
            vals['ContactType'] = self.ContactType
        if self.Country is not None:
            vals['Country'] = self.Country
        if self.Country2 is not None:
            vals['Country2'] = self.Country2
        if self.Country3 is not None:
            vals['Country3'] = self.Country3
        if self.CreatedBy is not None:
            vals['CreatedBy'] = self.CreatedBy
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.Email is not None:
            vals['Email'] = self.Email
        if self.EmailAddress2 is not None:
            vals['EmailAddress2'] = self.EmailAddress2
        if self.EmailAddress3 is not None:
            vals['EmailAddress3'] = self.EmailAddress3
        if self.Fax1 is not None:
            vals['Fax1'] = self.Fax1
        if self.Fax1Type is not None:
            vals['Fax1Type'] = self.Fax1Type
        if self.Fax2 is not None:
            vals['Fax2'] = self.Fax2
        if self.Fax2Type is not None:
            vals['Fax2Type'] = self.Fax2Type
        if self.FirstName is not None:
            vals['FirstName'] = self.FirstName
        if self.Groups is not None:
            vals['Groups'] = self.Groups
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.JobTitle is not None:
            vals['JobTitle'] = self.JobTitle
        if self.LastName is not None:
            vals['LastName'] = self.LastName
        if self.LastUpdated is not None:
            vals['LastUpdated'] = self.LastUpdated
        if self.LastUpdatedBy is not None:
            vals['LastUpdatedBy'] = self.LastUpdatedBy
        if self.LeadSourceId is not None:
            vals['LeadSourceId'] = self.LeadSourceId
        if self.Leadsource is not None:
            vals['Leadsource'] = self.Leadsource
        if self.MiddleName is not None:
            vals['MiddleName'] = self.MiddleName
        if self.Nickname is not None:
            vals['Nickname'] = self.Nickname
        if self.OwnerID is not None:
            vals['OwnerID'] = self.OwnerID
        if self.Password is not None:
            vals['Password'] = self.Password
        if self.Phone1 is not None:
            vals['Phone1'] = self.Phone1
        if self.Phone1Ext is not None:
            vals['Phone1Ext'] = self.Phone1Ext
        if self.Phone1Type is not None:
            vals['Phone1Type'] = self.Phone1Type
        if self.Phone2 is not None:
            vals['Phone2'] = self.Phone2
        if self.Phone2Ext is not None:
            vals['Phone2Ext'] = self.Phone2Ext
        if self.Phone2Type is not None:
            vals['Phone2Type'] = self.Phone2Type
        if self.Phone3 is not None:
            vals['Phone3'] = self.Phone3
        if self.Phone3Ext is not None:
            vals['Phone3Ext'] = self.Phone3Ext
        if self.Phone3Type is not None:
            vals['Phone3Type'] = self.Phone3Type
        if self.Phone4 is not None:
            vals['Phone4'] = self.Phone4
        if self.Phone4Ext is not None:
            vals['Phone4Ext'] = self.Phone4Ext
        if self.Phone4Type is not None:
            vals['Phone4Type'] = self.Phone4Type
        if self.Phone5 is not None:
            vals['Phone5'] = self.Phone5
        if self.Phone5Ext is not None:
            vals['Phone5Ext'] = self.Phone5Ext
        if self.Phone5Type is not None:
            vals['Phone5Type'] = self.Phone5Type
        if self.PostalCode is not None:
            vals['PostalCode'] = self.PostalCode
        if self.PostalCode2 is not None:
            vals['PostalCode2'] = self.PostalCode2
        if self.PostalCode3 is not None:
            vals['PostalCode3'] = self.PostalCode3
        if self.ReferralCode is not None:
            vals['ReferralCode'] = self.ReferralCode
        if self.SpouseName is not None:
            vals['SpouseName'] = self.SpouseName
        if self.State is not None:
            vals['State'] = self.State
        if self.State2 is not None:
            vals['State2'] = self.State2
        if self.State3 is not None:
            vals['State3'] = self.State3
        if self.StreetAddress1 is not None:
            vals['StreetAddress1'] = self.StreetAddress1
        if self.StreetAddress2 is not None:
            vals['StreetAddress2'] = self.StreetAddress2
        if self.Suffix is not None:
            vals['Suffix'] = self.Suffix
        if self.Title is not None:
            vals['Title'] = self.Title
        if self.Username is not None:
            vals['Username'] = self.Username
        if self.Validated is not None:
            vals['Validated'] = self.Validated
        if self.Website is not None:
            vals['Website'] = self.Website
        if self.ZipFour1 is not None:
            vals['ZipFour1'] = self.ZipFour1
        if self.ZipFour2 is not None:
            vals['ZipFour2'] = self.ZipFour2
        if self.ZipFour3 is not None:
            vals['ZipFour3'] = self.ZipFour3
        return vals

    def _template(self):
        if self.AccountId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address2Street1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address2Street2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address3Street1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address3Street2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Address3Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Anniversary: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AssistantName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AssistantPhone: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillingInformation: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Birthday: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.City: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.City2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.City3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Company: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CompanyID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactNotes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Country: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Country2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Country3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Email: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Fax2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Groups: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.JobTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadSourceId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Leadsource: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MiddleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Nickname: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OwnerID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Password: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone3Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone3Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone4: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone4Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone4Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone5: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone5Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone5Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ReferralCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SpouseName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Suffix: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Username: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Validated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Website: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour3: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ContactAction(object):
    global contactactions
    def __init__(self, values):
        self.values=values
        if 'contactactions' not in globals():
            contactactions = []
        if 'Accepted' in values.keys():
            self.Accepted=values['Accepted']
        else:
            self.Accepted=None
        if 'ActionDate' in values.keys():
            self.ActionDate=values['ActionDate']
        else:
            self.ActionDate=None
        if 'ActionDescription' in values.keys():
            self.ActionDescription=values['ActionDescription']
        else:
            self.ActionDescription=None
        if 'ActionType' in values.keys():
            self.ActionType=values['ActionType']
        else:
            self.ActionType=None
        if 'CompletionDate' in values.keys():
            self.CompletionDate=values['CompletionDate']
        else:
            self.CompletionDate=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'CreatedBy' in values.keys():
            self.CreatedBy=values['CreatedBy']
        else:
            self.CreatedBy=None
        if 'CreationDate' in values.keys():
            self.CreationDate=values['CreationDate']
        else:
            self.CreationDate=None
        if 'CreationNotes' in values.keys():
            self.CreationNotes=values['CreationNotes']
        else:
            self.CreationNotes=None
        if 'EndDate' in values.keys():
            self.EndDate=values['EndDate']
        else:
            self.EndDate=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'IsAppointment' in values.keys():
            self.IsAppointment=values['IsAppointment']
        else:
            self.IsAppointment=None
        if 'LastUpdated' in values.keys():
            self.LastUpdated=values['LastUpdated']
        else:
            self.LastUpdated=None
        if 'LastUpdatedBy' in values.keys():
            self.LastUpdatedBy=values['LastUpdatedBy']
        else:
            self.LastUpdatedBy=None
        if 'ObjectType' in values.keys():
            self.ObjectType=values['ObjectType']
        else:
            self.ObjectType=None
        if 'OpportunityId' in values.keys():
            self.OpportunityId=values['OpportunityId']
        else:
            self.OpportunityId=None
        if 'PopupDate' in values.keys():
            self.PopupDate=values['PopupDate']
        else:
            self.PopupDate=None
        if 'Priority' in values.keys():
            self.Priority=values['Priority']
        else:
            self.Priority=None
        if 'UserID' in values.keys():
            self.UserID=values['UserID']
        else:
            self.UserID=None

    def prepare(self):
        vals={}
        if self.Accepted is not None:
            vals['Accepted'] = self.Accepted
        if self.ActionDate is not None:
            vals['ActionDate'] = self.ActionDate
        if self.ActionDescription is not None:
            vals['ActionDescription'] = self.ActionDescription
        if self.ActionType is not None:
            vals['ActionType'] = self.ActionType
        if self.CompletionDate is not None:
            vals['CompletionDate'] = self.CompletionDate
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.CreatedBy is not None:
            vals['CreatedBy'] = self.CreatedBy
        if self.CreationDate is not None:
            vals['CreationDate'] = self.CreationDate
        if self.CreationNotes is not None:
            vals['CreationNotes'] = self.CreationNotes
        if self.EndDate is not None:
            vals['EndDate'] = self.EndDate
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.IsAppointment is not None:
            vals['IsAppointment'] = self.IsAppointment
        if self.LastUpdated is not None:
            vals['LastUpdated'] = self.LastUpdated
        if self.LastUpdatedBy is not None:
            vals['LastUpdatedBy'] = self.LastUpdatedBy
        if self.ObjectType is not None:
            vals['ObjectType'] = self.ObjectType
        if self.OpportunityId is not None:
            vals['OpportunityId'] = self.OpportunityId
        if self.PopupDate is not None:
            vals['PopupDate'] = self.PopupDate
        if self.Priority is not None:
            vals['Priority'] = self.Priority
        if self.UserID is not None:
            vals['UserID'] = self.UserID
        return vals

    def _template(self):
        if self.Accepted: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ActionDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ActionDescription: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ActionType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CompletionDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreationDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreationNotes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EndDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.IsAppointment: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ObjectType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OpportunityId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PopupDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Priority: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.UserID: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ContactGroup(object):
    global contactgroups
    def __init__(self, values):
        self.values=values
        if 'contactgroups' not in globals():
            contactgroups = []
        if 'GroupCategoryId' in values.keys():
            self.GroupCategoryId=values['GroupCategoryId']
        else:
            self.GroupCategoryId=None
        if 'GroupDescription' in values.keys():
            self.GroupDescription=values['GroupDescription']
        else:
            self.GroupDescription=None
        if 'GroupName' in values.keys():
            self.GroupName=values['GroupName']
        else:
            self.GroupName=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None

    def prepare(self):
        vals={}
        if self.GroupCategoryId is not None:
            vals['GroupCategoryId'] = self.GroupCategoryId
        if self.GroupDescription is not None:
            vals['GroupDescription'] = self.GroupDescription
        if self.GroupName is not None:
            vals['GroupName'] = self.GroupName
        if self.Id is not None:
            vals['Id'] = self.Id
        return vals

    def _template(self):
        if self.GroupCategoryId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.GroupDescription: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.GroupName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ContactGroupAssign(object):
    global contactgroupassigns
    def __init__(self, values):
        self.values=values
        if 'contactgroupassigns' not in globals():
            contactgroupassigns = []
        if 'Contact.Address1Type'in values.keys():
            self.Contact_Address1Type=values['Contact.Address1Type']
        else:
            self.Contact_Address1Type=None
        if 'Contact.Address2Street1'in values.keys():
            self.Contact_Address2Street1=values['Contact.Address2Street1']
        else:
            self.Contact_Address2Street1=None
        if 'Contact.Address2Street2'in values.keys():
            self.Contact_Address2Street2=values['Contact.Address2Street2']
        else:
            self.Contact_Address2Street2=None
        if 'Contact.Address2Type'in values.keys():
            self.Contact_Address2Type=values['Contact.Address2Type']
        else:
            self.Contact_Address2Type=None
        if 'Contact.Address3Street1'in values.keys():
            self.Contact_Address3Street1=values['Contact.Address3Street1']
        else:
            self.Contact_Address3Street1=None
        if 'Contact.Address3Street2'in values.keys():
            self.Contact_Address3Street2=values['Contact.Address3Street2']
        else:
            self.Contact_Address3Street2=None
        if 'Contact.Address3Type'in values.keys():
            self.Contact_Address3Type=values['Contact.Address3Type']
        else:
            self.Contact_Address3Type=None
        if 'Contact.Anniversary'in values.keys():
            self.Contact_Anniversary=values['Contact.Anniversary']
        else:
            self.Contact_Anniversary=None
        if 'Contact.AssistantName'in values.keys():
            self.Contact_AssistantName=values['Contact.AssistantName']
        else:
            self.Contact_AssistantName=None
        if 'Contact.AssistantPhone'in values.keys():
            self.Contact_AssistantPhone=values['Contact.AssistantPhone']
        else:
            self.Contact_AssistantPhone=None
        if 'Contact.BillingInformation'in values.keys():
            self.Contact_BillingInformation=values['Contact.BillingInformation']
        else:
            self.Contact_BillingInformation=None
        if 'Contact.Birthday'in values.keys():
            self.Contact_Birthday=values['Contact.Birthday']
        else:
            self.Contact_Birthday=None
        if 'Contact.City'in values.keys():
            self.Contact_City=values['Contact.City']
        else:
            self.Contact_City=None
        if 'Contact.City2'in values.keys():
            self.Contact_City2=values['Contact.City2']
        else:
            self.Contact_City2=None
        if 'Contact.City3'in values.keys():
            self.Contact_City3=values['Contact.City3']
        else:
            self.Contact_City3=None
        if 'Contact.Company'in values.keys():
            self.Contact_Company=values['Contact.Company']
        else:
            self.Contact_Company=None
        if 'Contact.CompanyID'in values.keys():
            self.Contact_CompanyID=values['Contact.CompanyID']
        else:
            self.Contact_CompanyID=None
        if 'Contact.ContactNotes'in values.keys():
            self.Contact_ContactNotes=values['Contact.ContactNotes']
        else:
            self.Contact_ContactNotes=None
        if 'Contact.ContactType'in values.keys():
            self.Contact_ContactType=values['Contact.ContactType']
        else:
            self.Contact_ContactType=None
        if 'Contact.Country'in values.keys():
            self.Contact_Country=values['Contact.Country']
        else:
            self.Contact_Country=None
        if 'Contact.Country2'in values.keys():
            self.Contact_Country2=values['Contact.Country2']
        else:
            self.Contact_Country2=None
        if 'Contact.Country3'in values.keys():
            self.Contact_Country3=values['Contact.Country3']
        else:
            self.Contact_Country3=None
        if 'Contact.CreatedBy'in values.keys():
            self.Contact_CreatedBy=values['Contact.CreatedBy']
        else:
            self.Contact_CreatedBy=None
        if 'Contact.CustomDate1'in values.keys():
            self.Contact_CustomDate1=values['Contact.CustomDate1']
        else:
            self.Contact_CustomDate1=None
        if 'Contact.CustomDate2'in values.keys():
            self.Contact_CustomDate2=values['Contact.CustomDate2']
        else:
            self.Contact_CustomDate2=None
        if 'Contact.CustomDate3'in values.keys():
            self.Contact_CustomDate3=values['Contact.CustomDate3']
        else:
            self.Contact_CustomDate3=None
        if 'Contact.CustomDate4'in values.keys():
            self.Contact_CustomDate4=values['Contact.CustomDate4']
        else:
            self.Contact_CustomDate4=None
        if 'Contact.CustomDate5'in values.keys():
            self.Contact_CustomDate5=values['Contact.CustomDate5']
        else:
            self.Contact_CustomDate5=None
        if 'Contact.CustomDbl1'in values.keys():
            self.Contact_CustomDbl1=values['Contact.CustomDbl1']
        else:
            self.Contact_CustomDbl1=None
        if 'Contact.CustomDbl2'in values.keys():
            self.Contact_CustomDbl2=values['Contact.CustomDbl2']
        else:
            self.Contact_CustomDbl2=None
        if 'Contact.CustomDbl3'in values.keys():
            self.Contact_CustomDbl3=values['Contact.CustomDbl3']
        else:
            self.Contact_CustomDbl3=None
        if 'Contact.CustomDbl4'in values.keys():
            self.Contact_CustomDbl4=values['Contact.CustomDbl4']
        else:
            self.Contact_CustomDbl4=None
        if 'Contact.CustomDbl5'in values.keys():
            self.Contact_CustomDbl5=values['Contact.CustomDbl5']
        else:
            self.Contact_CustomDbl5=None
        if 'Contact.CustomField1'in values.keys():
            self.Contact_CustomField1=values['Contact.CustomField1']
        else:
            self.Contact_CustomField1=None
        if 'Contact.CustomField10'in values.keys():
            self.Contact_CustomField10=values['Contact.CustomField10']
        else:
            self.Contact_CustomField10=None
        if 'Contact.CustomField2'in values.keys():
            self.Contact_CustomField2=values['Contact.CustomField2']
        else:
            self.Contact_CustomField2=None
        if 'Contact.CustomField3'in values.keys():
            self.Contact_CustomField3=values['Contact.CustomField3']
        else:
            self.Contact_CustomField3=None
        if 'Contact.CustomField4'in values.keys():
            self.Contact_CustomField4=values['Contact.CustomField4']
        else:
            self.Contact_CustomField4=None
        if 'Contact.CustomField5'in values.keys():
            self.Contact_CustomField5=values['Contact.CustomField5']
        else:
            self.Contact_CustomField5=None
        if 'Contact.CustomField6'in values.keys():
            self.Contact_CustomField6=values['Contact.CustomField6']
        else:
            self.Contact_CustomField6=None
        if 'Contact.CustomField7'in values.keys():
            self.Contact_CustomField7=values['Contact.CustomField7']
        else:
            self.Contact_CustomField7=None
        if 'Contact.CustomField8'in values.keys():
            self.Contact_CustomField8=values['Contact.CustomField8']
        else:
            self.Contact_CustomField8=None
        if 'Contact.CustomField9'in values.keys():
            self.Contact_CustomField9=values['Contact.CustomField9']
        else:
            self.Contact_CustomField9=None
        if 'Contact.DateCreated'in values.keys():
            self.Contact_DateCreated=values['Contact.DateCreated']
        else:
            self.Contact_DateCreated=None
        if 'Contact.Email'in values.keys():
            self.Contact_Email=values['Contact.Email']
        else:
            self.Contact_Email=None
        if 'Contact.EmailAddress2'in values.keys():
            self.Contact_EmailAddress2=values['Contact.EmailAddress2']
        else:
            self.Contact_EmailAddress2=None
        if 'Contact.EmailAddress3'in values.keys():
            self.Contact_EmailAddress3=values['Contact.EmailAddress3']
        else:
            self.Contact_EmailAddress3=None
        if 'Contact.Fax1'in values.keys():
            self.Contact_Fax1=values['Contact.Fax1']
        else:
            self.Contact_Fax1=None
        if 'Contact.Fax1Type'in values.keys():
            self.Contact_Fax1Type=values['Contact.Fax1Type']
        else:
            self.Contact_Fax1Type=None
        if 'Contact.Fax2'in values.keys():
            self.Contact_Fax2=values['Contact.Fax2']
        else:
            self.Contact_Fax2=None
        if 'Contact.Fax2Type'in values.keys():
            self.Contact_Fax2Type=values['Contact.Fax2Type']
        else:
            self.Contact_Fax2Type=None
        if 'Contact.FirstName'in values.keys():
            self.Contact_FirstName=values['Contact.FirstName']
        else:
            self.Contact_FirstName=None
        if 'Contact.Groups'in values.keys():
            self.Contact_Groups=values['Contact.Groups']
        else:
            self.Contact_Groups=None
        if 'Contact.HTMLSignature'in values.keys():
            self.Contact_HTMLSignature=values['Contact.HTMLSignature']
        else:
            self.Contact_HTMLSignature=None
        if 'Contact.Id'in values.keys():
            self.Contact_Id=values['Contact.Id']
        else:
            self.Contact_Id=None
        if 'Contact.JobTitle'in values.keys():
            self.Contact_JobTitle=values['Contact.JobTitle']
        else:
            self.Contact_JobTitle=None
        if 'Contact.LastName'in values.keys():
            self.Contact_LastName=values['Contact.LastName']
        else:
            self.Contact_LastName=None
        if 'Contact.LastUpdated'in values.keys():
            self.Contact_LastUpdated=values['Contact.LastUpdated']
        else:
            self.Contact_LastUpdated=None
        if 'Contact.LastUpdatedBy'in values.keys():
            self.Contact_LastUpdatedBy=values['Contact.LastUpdatedBy']
        else:
            self.Contact_LastUpdatedBy=None
        if 'Contact.Leadsource'in values.keys():
            self.Contact_Leadsource=values['Contact.Leadsource']
        else:
            self.Contact_Leadsource=None
        if 'Contact.MiddleName'in values.keys():
            self.Contact_MiddleName=values['Contact.MiddleName']
        else:
            self.Contact_MiddleName=None
        if 'Contact.Nickname'in values.keys():
            self.Contact_Nickname=values['Contact.Nickname']
        else:
            self.Contact_Nickname=None
        if 'Contact.OwnerID'in values.keys():
            self.Contact_OwnerID=values['Contact.OwnerID']
        else:
            self.Contact_OwnerID=None
        if 'Contact.Phone1'in values.keys():
            self.Contact_Phone1=values['Contact.Phone1']
        else:
            self.Contact_Phone1=None
        if 'Contact.Phone1Ext'in values.keys():
            self.Contact_Phone1Ext=values['Contact.Phone1Ext']
        else:
            self.Contact_Phone1Ext=None
        if 'Contact.Phone1Type'in values.keys():
            self.Contact_Phone1Type=values['Contact.Phone1Type']
        else:
            self.Contact_Phone1Type=None
        if 'Contact.Phone2'in values.keys():
            self.Contact_Phone2=values['Contact.Phone2']
        else:
            self.Contact_Phone2=None
        if 'Contact.Phone2Ext'in values.keys():
            self.Contact_Phone2Ext=values['Contact.Phone2Ext']
        else:
            self.Contact_Phone2Ext=None
        if 'Contact.Phone2Type'in values.keys():
            self.Contact_Phone2Type=values['Contact.Phone2Type']
        else:
            self.Contact_Phone2Type=None
        if 'Contact.Phone3'in values.keys():
            self.Contact_Phone3=values['Contact.Phone3']
        else:
            self.Contact_Phone3=None
        if 'Contact.Phone3Ext'in values.keys():
            self.Contact_Phone3Ext=values['Contact.Phone3Ext']
        else:
            self.Contact_Phone3Ext=None
        if 'Contact.Phone3Type'in values.keys():
            self.Contact_Phone3Type=values['Contact.Phone3Type']
        else:
            self.Contact_Phone3Type=None
        if 'Contact.Phone4'in values.keys():
            self.Contact_Phone4=values['Contact.Phone4']
        else:
            self.Contact_Phone4=None
        if 'Contact.Phone4Ext'in values.keys():
            self.Contact_Phone4Ext=values['Contact.Phone4Ext']
        else:
            self.Contact_Phone4Ext=None
        if 'Contact.Phone4Type'in values.keys():
            self.Contact_Phone4Type=values['Contact.Phone4Type']
        else:
            self.Contact_Phone4Type=None
        if 'Contact.Phone5'in values.keys():
            self.Contact_Phone5=values['Contact.Phone5']
        else:
            self.Contact_Phone5=None
        if 'Contact.Phone5Ext'in values.keys():
            self.Contact_Phone5Ext=values['Contact.Phone5Ext']
        else:
            self.Contact_Phone5Ext=None
        if 'Contact.Phone5Type'in values.keys():
            self.Contact_Phone5Type=values['Contact.Phone5Type']
        else:
            self.Contact_Phone5Type=None
        if 'Contact.PostalCode'in values.keys():
            self.Contact_PostalCode=values['Contact.PostalCode']
        else:
            self.Contact_PostalCode=None
        if 'Contact.PostalCode2'in values.keys():
            self.Contact_PostalCode2=values['Contact.PostalCode2']
        else:
            self.Contact_PostalCode2=None
        if 'Contact.PostalCode3'in values.keys():
            self.Contact_PostalCode3=values['Contact.PostalCode3']
        else:
            self.Contact_PostalCode3=None
        if 'Contact.ReferralCode'in values.keys():
            self.Contact_ReferralCode=values['Contact.ReferralCode']
        else:
            self.Contact_ReferralCode=None
        if 'Contact.Signature'in values.keys():
            self.Contact_Signature=values['Contact.Signature']
        else:
            self.Contact_Signature=None
        if 'Contact.SpouseName'in values.keys():
            self.Contact_SpouseName=values['Contact.SpouseName']
        else:
            self.Contact_SpouseName=None
        if 'Contact.State'in values.keys():
            self.Contact_State=values['Contact.State']
        else:
            self.Contact_State=None
        if 'Contact.State2'in values.keys():
            self.Contact_State2=values['Contact.State2']
        else:
            self.Contact_State2=None
        if 'Contact.State3'in values.keys():
            self.Contact_State3=values['Contact.State3']
        else:
            self.Contact_State3=None
        if 'Contact.StreetAddress1'in values.keys():
            self.Contact_StreetAddress1=values['Contact.StreetAddress1']
        else:
            self.Contact_StreetAddress1=None
        if 'Contact.StreetAddress2'in values.keys():
            self.Contact_StreetAddress2=values['Contact.StreetAddress2']
        else:
            self.Contact_StreetAddress2=None
        if 'Contact.Suffix'in values.keys():
            self.Contact_Suffix=values['Contact.Suffix']
        else:
            self.Contact_Suffix=None
        if 'Contact.Title'in values.keys():
            self.Contact_Title=values['Contact.Title']
        else:
            self.Contact_Title=None
        if 'Contact.Website'in values.keys():
            self.Contact_Website=values['Contact.Website']
        else:
            self.Contact_Website=None
        if 'Contact.ZipFour1'in values.keys():
            self.Contact_ZipFour1=values['Contact.ZipFour1']
        else:
            self.Contact_ZipFour1=None
        if 'Contact.ZipFour2'in values.keys():
            self.Contact_ZipFour2=values['Contact.ZipFour2']
        else:
            self.Contact_ZipFour2=None
        if 'Contact.ZipFour3'in values.keys():
            self.Contact_ZipFour3=values['Contact.ZipFour3']
        else:
            self.Contact_ZipFour3=None
        if 'ContactGroup' in values.keys():
            self.ContactGroup=values['ContactGroup']
        else:
            self.ContactGroup=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'GroupId' in values.keys():
            self.GroupId=values['GroupId']
        else:
            self.GroupId=None

    def prepare(self):
        vals={}
        if self.Contact_Address1Type is not None:
            vals['Contact.Address1Type'] = self.Contact_Address1Type
        if self.Contact_Address2Street1 is not None:
            vals['Contact.Address2Street1'] = self.Contact_Address2Street1
        if self.Contact_Address2Street2 is not None:
            vals['Contact.Address2Street2'] = self.Contact_Address2Street2
        if self.Contact_Address2Type is not None:
            vals['Contact.Address2Type'] = self.Contact_Address2Type
        if self.Contact_Address3Street1 is not None:
            vals['Contact.Address3Street1'] = self.Contact_Address3Street1
        if self.Contact_Address3Street2 is not None:
            vals['Contact.Address3Street2'] = self.Contact_Address3Street2
        if self.Contact_Address3Type is not None:
            vals['Contact.Address3Type'] = self.Contact_Address3Type
        if self.Contact_Anniversary is not None:
            vals['Contact.Anniversary'] = self.Contact_Anniversary
        if self.Contact_AssistantName is not None:
            vals['Contact.AssistantName'] = self.Contact_AssistantName
        if self.Contact_AssistantPhone is not None:
            vals['Contact.AssistantPhone'] = self.Contact_AssistantPhone
        if self.Contact_BillingInformation is not None:
            vals['Contact.BillingInformation'] = self.Contact_BillingInformation
        if self.Contact_Birthday is not None:
            vals['Contact.Birthday'] = self.Contact_Birthday
        if self.Contact_City is not None:
            vals['Contact.City'] = self.Contact_City
        if self.Contact_City2 is not None:
            vals['Contact.City2'] = self.Contact_City2
        if self.Contact_City3 is not None:
            vals['Contact.City3'] = self.Contact_City3
        if self.Contact_Company is not None:
            vals['Contact.Company'] = self.Contact_Company
        if self.Contact_CompanyID is not None:
            vals['Contact.CompanyID'] = self.Contact_CompanyID
        if self.Contact_ContactNotes is not None:
            vals['Contact.ContactNotes'] = self.Contact_ContactNotes
        if self.Contact_ContactType is not None:
            vals['Contact.ContactType'] = self.Contact_ContactType
        if self.Contact_Country is not None:
            vals['Contact.Country'] = self.Contact_Country
        if self.Contact_Country2 is not None:
            vals['Contact.Country2'] = self.Contact_Country2
        if self.Contact_Country3 is not None:
            vals['Contact.Country3'] = self.Contact_Country3
        if self.Contact_CreatedBy is not None:
            vals['Contact.CreatedBy'] = self.Contact_CreatedBy
        if self.Contact_CustomDate1 is not None:
            vals['Contact.CustomDate1'] = self.Contact_CustomDate1
        if self.Contact_CustomDate2 is not None:
            vals['Contact.CustomDate2'] = self.Contact_CustomDate2
        if self.Contact_CustomDate3 is not None:
            vals['Contact.CustomDate3'] = self.Contact_CustomDate3
        if self.Contact_CustomDate4 is not None:
            vals['Contact.CustomDate4'] = self.Contact_CustomDate4
        if self.Contact_CustomDate5 is not None:
            vals['Contact.CustomDate5'] = self.Contact_CustomDate5
        if self.Contact_CustomDbl1 is not None:
            vals['Contact.CustomDbl1'] = self.Contact_CustomDbl1
        if self.Contact_CustomDbl2 is not None:
            vals['Contact.CustomDbl2'] = self.Contact_CustomDbl2
        if self.Contact_CustomDbl3 is not None:
            vals['Contact.CustomDbl3'] = self.Contact_CustomDbl3
        if self.Contact_CustomDbl4 is not None:
            vals['Contact.CustomDbl4'] = self.Contact_CustomDbl4
        if self.Contact_CustomDbl5 is not None:
            vals['Contact.CustomDbl5'] = self.Contact_CustomDbl5
        if self.Contact_CustomField1 is not None:
            vals['Contact.CustomField1'] = self.Contact_CustomField1
        if self.Contact_CustomField10 is not None:
            vals['Contact.CustomField10'] = self.Contact_CustomField10
        if self.Contact_CustomField2 is not None:
            vals['Contact.CustomField2'] = self.Contact_CustomField2
        if self.Contact_CustomField3 is not None:
            vals['Contact.CustomField3'] = self.Contact_CustomField3
        if self.Contact_CustomField4 is not None:
            vals['Contact.CustomField4'] = self.Contact_CustomField4
        if self.Contact_CustomField5 is not None:
            vals['Contact.CustomField5'] = self.Contact_CustomField5
        if self.Contact_CustomField6 is not None:
            vals['Contact.CustomField6'] = self.Contact_CustomField6
        if self.Contact_CustomField7 is not None:
            vals['Contact.CustomField7'] = self.Contact_CustomField7
        if self.Contact_CustomField8 is not None:
            vals['Contact.CustomField8'] = self.Contact_CustomField8
        if self.Contact_CustomField9 is not None:
            vals['Contact.CustomField9'] = self.Contact_CustomField9
        if self.Contact_DateCreated is not None:
            vals['Contact.DateCreated'] = self.Contact_DateCreated
        if self.Contact_Email is not None:
            vals['Contact.Email'] = self.Contact_Email
        if self.Contact_EmailAddress2 is not None:
            vals['Contact.EmailAddress2'] = self.Contact_EmailAddress2
        if self.Contact_EmailAddress3 is not None:
            vals['Contact.EmailAddress3'] = self.Contact_EmailAddress3
        if self.Contact_Fax1 is not None:
            vals['Contact.Fax1'] = self.Contact_Fax1
        if self.Contact_Fax1Type is not None:
            vals['Contact.Fax1Type'] = self.Contact_Fax1Type
        if self.Contact_Fax2 is not None:
            vals['Contact.Fax2'] = self.Contact_Fax2
        if self.Contact_Fax2Type is not None:
            vals['Contact.Fax2Type'] = self.Contact_Fax2Type
        if self.Contact_FirstName is not None:
            vals['Contact.FirstName'] = self.Contact_FirstName
        if self.Contact_Groups is not None:
            vals['Contact.Groups'] = self.Contact_Groups
        if self.Contact_HTMLSignature is not None:
            vals['Contact.HTMLSignature'] = self.Contact_HTMLSignature
        if self.Contact_Id is not None:
            vals['Contact.Id'] = self.Contact_Id
        if self.Contact_JobTitle is not None:
            vals['Contact.JobTitle'] = self.Contact_JobTitle
        if self.Contact_LastName is not None:
            vals['Contact.LastName'] = self.Contact_LastName
        if self.Contact_LastUpdated is not None:
            vals['Contact.LastUpdated'] = self.Contact_LastUpdated
        if self.Contact_LastUpdatedBy is not None:
            vals['Contact.LastUpdatedBy'] = self.Contact_LastUpdatedBy
        if self.Contact_Leadsource is not None:
            vals['Contact.Leadsource'] = self.Contact_Leadsource
        if self.Contact_MiddleName is not None:
            vals['Contact.MiddleName'] = self.Contact_MiddleName
        if self.Contact_Nickname is not None:
            vals['Contact.Nickname'] = self.Contact_Nickname
        if self.Contact_OwnerID is not None:
            vals['Contact.OwnerID'] = self.Contact_OwnerID
        if self.Contact_Phone1 is not None:
            vals['Contact.Phone1'] = self.Contact_Phone1
        if self.Contact_Phone1Ext is not None:
            vals['Contact.Phone1Ext'] = self.Contact_Phone1Ext
        if self.Contact_Phone1Type is not None:
            vals['Contact.Phone1Type'] = self.Contact_Phone1Type
        if self.Contact_Phone2 is not None:
            vals['Contact.Phone2'] = self.Contact_Phone2
        if self.Contact_Phone2Ext is not None:
            vals['Contact.Phone2Ext'] = self.Contact_Phone2Ext
        if self.Contact_Phone2Type is not None:
            vals['Contact.Phone2Type'] = self.Contact_Phone2Type
        if self.Contact_Phone3 is not None:
            vals['Contact.Phone3'] = self.Contact_Phone3
        if self.Contact_Phone3Ext is not None:
            vals['Contact.Phone3Ext'] = self.Contact_Phone3Ext
        if self.Contact_Phone3Type is not None:
            vals['Contact.Phone3Type'] = self.Contact_Phone3Type
        if self.Contact_Phone4 is not None:
            vals['Contact.Phone4'] = self.Contact_Phone4
        if self.Contact_Phone4Ext is not None:
            vals['Contact.Phone4Ext'] = self.Contact_Phone4Ext
        if self.Contact_Phone4Type is not None:
            vals['Contact.Phone4Type'] = self.Contact_Phone4Type
        if self.Contact_Phone5 is not None:
            vals['Contact.Phone5'] = self.Contact_Phone5
        if self.Contact_Phone5Ext is not None:
            vals['Contact.Phone5Ext'] = self.Contact_Phone5Ext
        if self.Contact_Phone5Type is not None:
            vals['Contact.Phone5Type'] = self.Contact_Phone5Type
        if self.Contact_PostalCode is not None:
            vals['Contact.PostalCode'] = self.Contact_PostalCode
        if self.Contact_PostalCode2 is not None:
            vals['Contact.PostalCode2'] = self.Contact_PostalCode2
        if self.Contact_PostalCode3 is not None:
            vals['Contact.PostalCode3'] = self.Contact_PostalCode3
        if self.Contact_ReferralCode is not None:
            vals['Contact.ReferralCode'] = self.Contact_ReferralCode
        if self.Contact_Signature is not None:
            vals['Contact.Signature'] = self.Contact_Signature
        if self.Contact_SpouseName is not None:
            vals['Contact.SpouseName'] = self.Contact_SpouseName
        if self.Contact_State is not None:
            vals['Contact.State'] = self.Contact_State
        if self.Contact_State2 is not None:
            vals['Contact.State2'] = self.Contact_State2
        if self.Contact_State3 is not None:
            vals['Contact.State3'] = self.Contact_State3
        if self.Contact_StreetAddress1 is not None:
            vals['Contact.StreetAddress1'] = self.Contact_StreetAddress1
        if self.Contact_StreetAddress2 is not None:
            vals['Contact.StreetAddress2'] = self.Contact_StreetAddress2
        if self.Contact_Suffix is not None:
            vals['Contact.Suffix'] = self.Contact_Suffix
        if self.Contact_Title is not None:
            vals['Contact.Title'] = self.Contact_Title
        if self.Contact_Website is not None:
            vals['Contact.Website'] = self.Contact_Website
        if self.Contact_ZipFour1 is not None:
            vals['Contact.ZipFour1'] = self.Contact_ZipFour1
        if self.Contact_ZipFour2 is not None:
            vals['Contact.ZipFour2'] = self.Contact_ZipFour2
        if self.Contact_ZipFour3 is not None:
            vals['Contact.ZipFour3'] = self.Contact_ZipFour3
        if self.ContactGroup is not None:
            vals['ContactGroup'] = self.ContactGroup
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.GroupId is not None:
            vals['GroupId'] = self.GroupId
        return vals

    def _template(self):
        if self.Contact_Address1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Address2Street1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Address2Street2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Address2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Address3Street1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Address3Street2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Address3Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Anniversary: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_AssistantName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_AssistantPhone: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_BillingInformation: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Birthday: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_City: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_City2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_City3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Company: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CompanyID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_ContactNotes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_ContactType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Country: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Country2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Country3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CreatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDate1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDate2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDate3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDate4: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDate5: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDbl1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDbl2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDbl3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDbl4: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomDbl5: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField10: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField4: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField5: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField6: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField7: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField8: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_CustomField9: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Email: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_EmailAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_EmailAddress3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Fax1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Fax1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Fax2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Fax2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_FirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Groups: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_HTMLSignature: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_JobTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_LastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_LastUpdated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_LastUpdatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Leadsource: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_MiddleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Nickname: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_OwnerID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone1Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone2Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone3Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone3Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone4: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone4Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone4Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone5: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone5Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Phone5Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_PostalCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_PostalCode2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_PostalCode3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_ReferralCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Signature: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_SpouseName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_State: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_State2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_State3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_StreetAddress1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_StreetAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Suffix: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_Website: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_ZipFour1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_ZipFour2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Contact_ZipFour3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactGroup: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.GroupId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ContactGroupCategory(object):
    global contactgroupcategorys
    def __init__(self, values):
        self.values=values
        if 'contactgroupcategorys' not in globals():
            contactgroupcategorys = []
        if 'CategoryDescription' in values.keys():
            self.CategoryDescription=values['CategoryDescription']
        else:
            self.CategoryDescription=None
        if 'CategoryName' in values.keys():
            self.CategoryName=values['CategoryName']
        else:
            self.CategoryName=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None

    def prepare(self):
        vals={}
        if self.CategoryDescription is not None:
            vals['CategoryDescription'] = self.CategoryDescription
        if self.CategoryName is not None:
            vals['CategoryName'] = self.CategoryName
        if self.Id is not None:
            vals['Id'] = self.Id
        return vals

    def _template(self):
        if self.CategoryDescription: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CategoryName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class CreditCard(object):
    global creditcards
    def __init__(self, values):
        self.values=values
        if 'creditcards' not in globals():
            creditcards = []
        if 'BillAddress1' in values.keys():
            self.BillAddress1=values['BillAddress1']
        else:
            self.BillAddress1=None
        if 'BillAddress2' in values.keys():
            self.BillAddress2=values['BillAddress2']
        else:
            self.BillAddress2=None
        if 'BillCity' in values.keys():
            self.BillCity=values['BillCity']
        else:
            self.BillCity=None
        if 'BillCountry' in values.keys():
            self.BillCountry=values['BillCountry']
        else:
            self.BillCountry=None
        if 'BillName' in values.keys():
            self.BillName=values['BillName']
        else:
            self.BillName=None
        if 'BillState' in values.keys():
            self.BillState=values['BillState']
        else:
            self.BillState=None
        if 'BillZip' in values.keys():
            self.BillZip=values['BillZip']
        else:
            self.BillZip=None
        if 'CVV2' in values.keys():
            self.CVV2=values['CVV2']
        else:
            self.CVV2=None
        if 'CardNumber' in values.keys():
            self.CardNumber=values['CardNumber']
        else:
            self.CardNumber=None
        if 'CardType' in values.keys():
            self.CardType=values['CardType']
        else:
            self.CardType=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'Email' in values.keys():
            self.Email=values['Email']
        else:
            self.Email=None
        if 'ExpirationMonth' in values.keys():
            self.ExpirationMonth=values['ExpirationMonth']
        else:
            self.ExpirationMonth=None
        if 'ExpirationYear' in values.keys():
            self.ExpirationYear=values['ExpirationYear']
        else:
            self.ExpirationYear=None
        if 'FirstName' in values.keys():
            self.FirstName=values['FirstName']
        else:
            self.FirstName=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Last4' in values.keys():
            self.Last4=values['Last4']
        else:
            self.Last4=None
        if 'LastName' in values.keys():
            self.LastName=values['LastName']
        else:
            self.LastName=None
        if 'MaestroIssueNumber' in values.keys():
            self.MaestroIssueNumber=values['MaestroIssueNumber']
        else:
            self.MaestroIssueNumber=None
        if 'NameOnCard' in values.keys():
            self.NameOnCard=values['NameOnCard']
        else:
            self.NameOnCard=None
        if 'PhoneNumber' in values.keys():
            self.PhoneNumber=values['PhoneNumber']
        else:
            self.PhoneNumber=None
        if 'ShipAddress1' in values.keys():
            self.ShipAddress1=values['ShipAddress1']
        else:
            self.ShipAddress1=None
        if 'ShipAddress2' in values.keys():
            self.ShipAddress2=values['ShipAddress2']
        else:
            self.ShipAddress2=None
        if 'ShipCity' in values.keys():
            self.ShipCity=values['ShipCity']
        else:
            self.ShipCity=None
        if 'ShipCompanyName' in values.keys():
            self.ShipCompanyName=values['ShipCompanyName']
        else:
            self.ShipCompanyName=None
        if 'ShipCountry' in values.keys():
            self.ShipCountry=values['ShipCountry']
        else:
            self.ShipCountry=None
        if 'ShipFirstName' in values.keys():
            self.ShipFirstName=values['ShipFirstName']
        else:
            self.ShipFirstName=None
        if 'ShipLastName' in values.keys():
            self.ShipLastName=values['ShipLastName']
        else:
            self.ShipLastName=None
        if 'ShipMiddleName' in values.keys():
            self.ShipMiddleName=values['ShipMiddleName']
        else:
            self.ShipMiddleName=None
        if 'ShipName' in values.keys():
            self.ShipName=values['ShipName']
        else:
            self.ShipName=None
        if 'ShipPhoneNumber' in values.keys():
            self.ShipPhoneNumber=values['ShipPhoneNumber']
        else:
            self.ShipPhoneNumber=None
        if 'ShipState' in values.keys():
            self.ShipState=values['ShipState']
        else:
            self.ShipState=None
        if 'ShipZip' in values.keys():
            self.ShipZip=values['ShipZip']
        else:
            self.ShipZip=None
        if 'StartDateMonth' in values.keys():
            self.StartDateMonth=values['StartDateMonth']
        else:
            self.StartDateMonth=None
        if 'StartDateYear' in values.keys():
            self.StartDateYear=values['StartDateYear']
        else:
            self.StartDateYear=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None

    def prepare(self):
        vals={}
        if self.BillAddress1 is not None:
            vals['BillAddress1'] = self.BillAddress1
        if self.BillAddress2 is not None:
            vals['BillAddress2'] = self.BillAddress2
        if self.BillCity is not None:
            vals['BillCity'] = self.BillCity
        if self.BillCountry is not None:
            vals['BillCountry'] = self.BillCountry
        if self.BillName is not None:
            vals['BillName'] = self.BillName
        if self.BillState is not None:
            vals['BillState'] = self.BillState
        if self.BillZip is not None:
            vals['BillZip'] = self.BillZip
        if self.CVV2 is not None:
            vals['CVV2'] = self.CVV2
        if self.CardNumber is not None:
            vals['CardNumber'] = self.CardNumber
        if self.CardType is not None:
            vals['CardType'] = self.CardType
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.Email is not None:
            vals['Email'] = self.Email
        if self.ExpirationMonth is not None:
            vals['ExpirationMonth'] = self.ExpirationMonth
        if self.ExpirationYear is not None:
            vals['ExpirationYear'] = self.ExpirationYear
        if self.FirstName is not None:
            vals['FirstName'] = self.FirstName
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Last4 is not None:
            vals['Last4'] = self.Last4
        if self.LastName is not None:
            vals['LastName'] = self.LastName
        if self.MaestroIssueNumber is not None:
            vals['MaestroIssueNumber'] = self.MaestroIssueNumber
        if self.NameOnCard is not None:
            vals['NameOnCard'] = self.NameOnCard
        if self.PhoneNumber is not None:
            vals['PhoneNumber'] = self.PhoneNumber
        if self.ShipAddress1 is not None:
            vals['ShipAddress1'] = self.ShipAddress1
        if self.ShipAddress2 is not None:
            vals['ShipAddress2'] = self.ShipAddress2
        if self.ShipCity is not None:
            vals['ShipCity'] = self.ShipCity
        if self.ShipCompanyName is not None:
            vals['ShipCompanyName'] = self.ShipCompanyName
        if self.ShipCountry is not None:
            vals['ShipCountry'] = self.ShipCountry
        if self.ShipFirstName is not None:
            vals['ShipFirstName'] = self.ShipFirstName
        if self.ShipLastName is not None:
            vals['ShipLastName'] = self.ShipLastName
        if self.ShipMiddleName is not None:
            vals['ShipMiddleName'] = self.ShipMiddleName
        if self.ShipName is not None:
            vals['ShipName'] = self.ShipName
        if self.ShipPhoneNumber is not None:
            vals['ShipPhoneNumber'] = self.ShipPhoneNumber
        if self.ShipState is not None:
            vals['ShipState'] = self.ShipState
        if self.ShipZip is not None:
            vals['ShipZip'] = self.ShipZip
        if self.StartDateMonth is not None:
            vals['StartDateMonth'] = self.StartDateMonth
        if self.StartDateYear is not None:
            vals['StartDateYear'] = self.StartDateYear
        if self.Status is not None:
            vals['Status'] = self.Status
        return vals

    def _template(self):
        if self.BillAddress1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillCity: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillCountry: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillState: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillZip: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CVV2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CardNumber: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CardType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Email: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ExpirationMonth: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ExpirationYear: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Last4: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MaestroIssueNumber: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NameOnCard: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PhoneNumber: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipAddress1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipCity: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipCompanyName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipCountry: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipFirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipLastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipMiddleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipPhoneNumber: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipState: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipZip: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDateMonth: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDateYear: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class DataFormField(object):
    global dataformfields
    def __init__(self, values):
        self.values=values
        if 'dataformfields' not in globals():
            dataformfields = []
        if 'DataType' in values.keys():
            self.DataType=values['DataType']
        else:
            self.DataType=None
        if 'DefaultValue' in values.keys():
            self.DefaultValue=values['DefaultValue']
        else:
            self.DefaultValue=None
        if 'FormId' in values.keys():
            self.FormId=values['FormId']
        else:
            self.FormId=None
        if 'GroupId' in values.keys():
            self.GroupId=values['GroupId']
        else:
            self.GroupId=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Label' in values.keys():
            self.Label=values['Label']
        else:
            self.Label=None
        if 'ListRows' in values.keys():
            self.ListRows=values['ListRows']
        else:
            self.ListRows=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None
        if 'Values' in values.keys():
            self.Values=values['Values']
        else:
            self.Values=None

    def prepare(self):
        vals={}
        if self.DataType is not None:
            vals['DataType'] = self.DataType
        if self.DefaultValue is not None:
            vals['DefaultValue'] = self.DefaultValue
        if self.FormId is not None:
            vals['FormId'] = self.FormId
        if self.GroupId is not None:
            vals['GroupId'] = self.GroupId
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Label is not None:
            vals['Label'] = self.Label
        if self.ListRows is not None:
            vals['ListRows'] = self.ListRows
        if self.Name is not None:
            vals['Name'] = self.Name
        if self.Values is not None:
            vals['Values'] = self.Values
        return vals

    def _template(self):
        if self.DataType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DefaultValue: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FormId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.GroupId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Label: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ListRows: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Values: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class DataFormGroup(object):
    global dataformgroups
    def __init__(self, values):
        self.values=values
        if 'dataformgroups' not in globals():
            dataformgroups = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None
        if 'TabId' in values.keys():
            self.TabId=values['TabId']
        else:
            self.TabId=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Name is not None:
            vals['Name'] = self.Name
        if self.TabId is not None:
            vals['TabId'] = self.TabId
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TabId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class DataFormTab(object):
    global dataformtabs
    def __init__(self, values):
        self.values=values
        if 'dataformtabs' not in globals():
            dataformtabs = []
        if 'FormId' in values.keys():
            self.FormId=values['FormId']
        else:
            self.FormId=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'TabName' in values.keys():
            self.TabName=values['TabName']
        else:
            self.TabName=None

    def prepare(self):
        vals={}
        if self.FormId is not None:
            vals['FormId'] = self.FormId
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.TabName is not None:
            vals['TabName'] = self.TabName
        return vals

    def _template(self):
        if self.FormId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TabName: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Expense(object):
    global expenses
    def __init__(self, values):
        self.values=values
        if 'expenses' not in globals():
            expenses = []
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'DateIncurred' in values.keys():
            self.DateIncurred=values['DateIncurred']
        else:
            self.DateIncurred=None
        if 'ExpenseAmt' in values.keys():
            self.ExpenseAmt=values['ExpenseAmt']
        else:
            self.ExpenseAmt=None
        if 'ExpenseType' in values.keys():
            self.ExpenseType=values['ExpenseType']
        else:
            self.ExpenseType=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'TypeId' in values.keys():
            self.TypeId=values['TypeId']
        else:
            self.TypeId=None

    def prepare(self):
        vals={}
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.DateIncurred is not None:
            vals['DateIncurred'] = self.DateIncurred
        if self.ExpenseAmt is not None:
            vals['ExpenseAmt'] = self.ExpenseAmt
        if self.ExpenseType is not None:
            vals['ExpenseType'] = self.ExpenseType
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.TypeId is not None:
            vals['TypeId'] = self.TypeId
        return vals

    def _template(self):
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateIncurred: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ExpenseAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ExpenseType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TypeId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class FileBox(object):
    global fileboxs
    def __init__(self, values):
        self.values=values
        if 'fileboxs' not in globals():
            fileboxs = []
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'Extension' in values.keys():
            self.Extension=values['Extension']
        else:
            self.Extension=None
        if 'FileName' in values.keys():
            self.FileName=values['FileName']
        else:
            self.FileName=None
        if 'FileSize' in values.keys():
            self.FileSize=values['FileSize']
        else:
            self.FileSize=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Public' in values.keys():
            self.Public=values['Public']
        else:
            self.Public=None

    def prepare(self):
        vals={}
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.Extension is not None:
            vals['Extension'] = self.Extension
        if self.FileName is not None:
            vals['FileName'] = self.FileName
        if self.FileSize is not None:
            vals['FileSize'] = self.FileSize
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Public is not None:
            vals['Public'] = self.Public
        return vals

    def _template(self):
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Extension: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FileName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FileSize: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Public: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class GroupAssign(object):
    global groupassigns
    def __init__(self, values):
        self.values=values
        if 'groupassigns' not in globals():
            groupassigns = []
        if 'Admin' in values.keys():
            self.Admin=values['Admin']
        else:
            self.Admin=None
        if 'GroupId' in values.keys():
            self.GroupId=values['GroupId']
        else:
            self.GroupId=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'UserId' in values.keys():
            self.UserId=values['UserId']
        else:
            self.UserId=None

    def prepare(self):
        vals={}
        if self.Admin is not None:
            vals['Admin'] = self.Admin
        if self.GroupId is not None:
            vals['GroupId'] = self.GroupId
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.UserId is not None:
            vals['UserId'] = self.UserId
        return vals

    def _template(self):
        if self.Admin: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.GroupId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.UserId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Invoice(object):
    global invoices
    def __init__(self, values):
        self.values=values
        if 'invoices' not in globals():
            invoices = []
        if 'AffiliateId' in values.keys():
            self.AffiliateId=values['AffiliateId']
        else:
            self.AffiliateId=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'CreditStatus' in values.keys():
            self.CreditStatus=values['CreditStatus']
        else:
            self.CreditStatus=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'InvoiceTotal' in values.keys():
            self.InvoiceTotal=values['InvoiceTotal']
        else:
            self.InvoiceTotal=None
        if 'InvoiceType' in values.keys():
            self.InvoiceType=values['InvoiceType']
        else:
            self.InvoiceType=None
        if 'JobId' in values.keys():
            self.JobId=values['JobId']
        else:
            self.JobId=None
        if 'LeadAffiliateId' in values.keys():
            self.LeadAffiliateId=values['LeadAffiliateId']
        else:
            self.LeadAffiliateId=None
        if 'PayPlanStatus' in values.keys():
            self.PayPlanStatus=values['PayPlanStatus']
        else:
            self.PayPlanStatus=None
        if 'PayStatus' in values.keys():
            self.PayStatus=values['PayStatus']
        else:
            self.PayStatus=None
        if 'ProductSold' in values.keys():
            self.ProductSold=values['ProductSold']
        else:
            self.ProductSold=None
        if 'PromoCode' in values.keys():
            self.PromoCode=values['PromoCode']
        else:
            self.PromoCode=None
        if 'RefundStatus' in values.keys():
            self.RefundStatus=values['RefundStatus']
        else:
            self.RefundStatus=None
        if 'Synced' in values.keys():
            self.Synced=values['Synced']
        else:
            self.Synced=None
        if 'TotalDue' in values.keys():
            self.TotalDue=values['TotalDue']
        else:
            self.TotalDue=None
        if 'TotalPaid' in values.keys():
            self.TotalPaid=values['TotalPaid']
        else:
            self.TotalPaid=None

    def prepare(self):
        vals={}
        if self.AffiliateId is not None:
            vals['AffiliateId'] = self.AffiliateId
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.CreditStatus is not None:
            vals['CreditStatus'] = self.CreditStatus
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.InvoiceTotal is not None:
            vals['InvoiceTotal'] = self.InvoiceTotal
        if self.InvoiceType is not None:
            vals['InvoiceType'] = self.InvoiceType
        if self.JobId is not None:
            vals['JobId'] = self.JobId
        if self.LeadAffiliateId is not None:
            vals['LeadAffiliateId'] = self.LeadAffiliateId
        if self.PayPlanStatus is not None:
            vals['PayPlanStatus'] = self.PayPlanStatus
        if self.PayStatus is not None:
            vals['PayStatus'] = self.PayStatus
        if self.ProductSold is not None:
            vals['ProductSold'] = self.ProductSold
        if self.PromoCode is not None:
            vals['PromoCode'] = self.PromoCode
        if self.RefundStatus is not None:
            vals['RefundStatus'] = self.RefundStatus
        if self.Synced is not None:
            vals['Synced'] = self.Synced
        if self.TotalDue is not None:
            vals['TotalDue'] = self.TotalDue
        if self.TotalPaid is not None:
            vals['TotalPaid'] = self.TotalPaid
        return vals

    def _template(self):
        if self.AffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreditStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceTotal: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.JobId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadAffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayPlanStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductSold: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PromoCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.RefundStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Synced: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TotalDue: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TotalPaid: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class InvoiceItem(object):
    global invoiceitems
    def __init__(self, values):
        self.values=values
        if 'invoiceitems' not in globals():
            invoiceitems = []
        if 'CommissionStatus' in values.keys():
            self.CommissionStatus=values['CommissionStatus']
        else:
            self.CommissionStatus=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'Discount' in values.keys():
            self.Discount=values['Discount']
        else:
            self.Discount=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'InvoiceAmt' in values.keys():
            self.InvoiceAmt=values['InvoiceAmt']
        else:
            self.InvoiceAmt=None
        if 'InvoiceId' in values.keys():
            self.InvoiceId=values['InvoiceId']
        else:
            self.InvoiceId=None
        if 'OrderItemId' in values.keys():
            self.OrderItemId=values['OrderItemId']
        else:
            self.OrderItemId=None

    def prepare(self):
        vals={}
        if self.CommissionStatus is not None:
            vals['CommissionStatus'] = self.CommissionStatus
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.Discount is not None:
            vals['Discount'] = self.Discount
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.InvoiceAmt is not None:
            vals['InvoiceAmt'] = self.InvoiceAmt
        if self.InvoiceId is not None:
            vals['InvoiceId'] = self.InvoiceId
        if self.OrderItemId is not None:
            vals['OrderItemId'] = self.OrderItemId
        return vals

    def _template(self):
        if self.CommissionStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Discount: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OrderItemId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class InvoicePayment(object):
    global invoicepayments
    def __init__(self, values):
        self.values=values
        if 'invoicepayments' not in globals():
            invoicepayments = []
        if 'Amt' in values.keys():
            self.Amt=values['Amt']
        else:
            self.Amt=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'InvoiceId' in values.keys():
            self.InvoiceId=values['InvoiceId']
        else:
            self.InvoiceId=None
        if 'PayDate' in values.keys():
            self.PayDate=values['PayDate']
        else:
            self.PayDate=None
        if 'PayStatus' in values.keys():
            self.PayStatus=values['PayStatus']
        else:
            self.PayStatus=None
        if 'PaymentId' in values.keys():
            self.PaymentId=values['PaymentId']
        else:
            self.PaymentId=None
        if 'SkipCommission' in values.keys():
            self.SkipCommission=values['SkipCommission']
        else:
            self.SkipCommission=None

    def prepare(self):
        vals={}
        if self.Amt is not None:
            vals['Amt'] = self.Amt
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.InvoiceId is not None:
            vals['InvoiceId'] = self.InvoiceId
        if self.PayDate is not None:
            vals['PayDate'] = self.PayDate
        if self.PayStatus is not None:
            vals['PayStatus'] = self.PayStatus
        if self.PaymentId is not None:
            vals['PaymentId'] = self.PaymentId
        if self.SkipCommission is not None:
            vals['SkipCommission'] = self.SkipCommission
        return vals

    def _template(self):
        if self.Amt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PaymentId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SkipCommission: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Job(object):
    global jobs
    def __init__(self, values):
        self.values=values
        if 'jobs' not in globals():
            jobs = []
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'DueDate' in values.keys():
            self.DueDate=values['DueDate']
        else:
            self.DueDate=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'JobNotes' in values.keys():
            self.JobNotes=values['JobNotes']
        else:
            self.JobNotes=None
        if 'JobRecurringId' in values.keys():
            self.JobRecurringId=values['JobRecurringId']
        else:
            self.JobRecurringId=None
        if 'JobStatus' in values.keys():
            self.JobStatus=values['JobStatus']
        else:
            self.JobStatus=None
        if 'JobTitle' in values.keys():
            self.JobTitle=values['JobTitle']
        else:
            self.JobTitle=None
        if 'OrderStatus' in values.keys():
            self.OrderStatus=values['OrderStatus']
        else:
            self.OrderStatus=None
        if 'OrderType' in values.keys():
            self.OrderType=values['OrderType']
        else:
            self.OrderType=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'ShipCity' in values.keys():
            self.ShipCity=values['ShipCity']
        else:
            self.ShipCity=None
        if 'ShipCompany' in values.keys():
            self.ShipCompany=values['ShipCompany']
        else:
            self.ShipCompany=None
        if 'ShipCountry' in values.keys():
            self.ShipCountry=values['ShipCountry']
        else:
            self.ShipCountry=None
        if 'ShipFirstName' in values.keys():
            self.ShipFirstName=values['ShipFirstName']
        else:
            self.ShipFirstName=None
        if 'ShipLastName' in values.keys():
            self.ShipLastName=values['ShipLastName']
        else:
            self.ShipLastName=None
        if 'ShipMiddleName' in values.keys():
            self.ShipMiddleName=values['ShipMiddleName']
        else:
            self.ShipMiddleName=None
        if 'ShipPhone' in values.keys():
            self.ShipPhone=values['ShipPhone']
        else:
            self.ShipPhone=None
        if 'ShipState' in values.keys():
            self.ShipState=values['ShipState']
        else:
            self.ShipState=None
        if 'ShipStreet1' in values.keys():
            self.ShipStreet1=values['ShipStreet1']
        else:
            self.ShipStreet1=None
        if 'ShipStreet2' in values.keys():
            self.ShipStreet2=values['ShipStreet2']
        else:
            self.ShipStreet2=None
        if 'ShipZip' in values.keys():
            self.ShipZip=values['ShipZip']
        else:
            self.ShipZip=None
        if 'StartDate' in values.keys():
            self.StartDate=values['StartDate']
        else:
            self.StartDate=None

    def prepare(self):
        vals={}
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.DueDate is not None:
            vals['DueDate'] = self.DueDate
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.JobNotes is not None:
            vals['JobNotes'] = self.JobNotes
        if self.JobRecurringId is not None:
            vals['JobRecurringId'] = self.JobRecurringId
        if self.JobStatus is not None:
            vals['JobStatus'] = self.JobStatus
        if self.JobTitle is not None:
            vals['JobTitle'] = self.JobTitle
        if self.OrderStatus is not None:
            vals['OrderStatus'] = self.OrderStatus
        if self.OrderType is not None:
            vals['OrderType'] = self.OrderType
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.ShipCity is not None:
            vals['ShipCity'] = self.ShipCity
        if self.ShipCompany is not None:
            vals['ShipCompany'] = self.ShipCompany
        if self.ShipCountry is not None:
            vals['ShipCountry'] = self.ShipCountry
        if self.ShipFirstName is not None:
            vals['ShipFirstName'] = self.ShipFirstName
        if self.ShipLastName is not None:
            vals['ShipLastName'] = self.ShipLastName
        if self.ShipMiddleName is not None:
            vals['ShipMiddleName'] = self.ShipMiddleName
        if self.ShipPhone is not None:
            vals['ShipPhone'] = self.ShipPhone
        if self.ShipState is not None:
            vals['ShipState'] = self.ShipState
        if self.ShipStreet1 is not None:
            vals['ShipStreet1'] = self.ShipStreet1
        if self.ShipStreet2 is not None:
            vals['ShipStreet2'] = self.ShipStreet2
        if self.ShipZip is not None:
            vals['ShipZip'] = self.ShipZip
        if self.StartDate is not None:
            vals['StartDate'] = self.StartDate
        return vals

    def _template(self):
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DueDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.JobNotes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.JobRecurringId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.JobStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.JobTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OrderStatus: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OrderType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipCity: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipCompany: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipCountry: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipFirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipLastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipMiddleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipPhone: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipState: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipStreet1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipStreet2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShipZip: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class JobRecurringInstance(object):
    global jobrecurringinstances
    def __init__(self, values):
        self.values=values
        if 'jobrecurringinstances' not in globals():
            jobrecurringinstances = []
        if 'AutoCharge' in values.keys():
            self.AutoCharge=values['AutoCharge']
        else:
            self.AutoCharge=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'EndDate' in values.keys():
            self.EndDate=values['EndDate']
        else:
            self.EndDate=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'InvoiceItemId' in values.keys():
            self.InvoiceItemId=values['InvoiceItemId']
        else:
            self.InvoiceItemId=None
        if 'RecurringId' in values.keys():
            self.RecurringId=values['RecurringId']
        else:
            self.RecurringId=None
        if 'StartDate' in values.keys():
            self.StartDate=values['StartDate']
        else:
            self.StartDate=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None

    def prepare(self):
        vals={}
        if self.AutoCharge is not None:
            vals['AutoCharge'] = self.AutoCharge
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.EndDate is not None:
            vals['EndDate'] = self.EndDate
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.InvoiceItemId is not None:
            vals['InvoiceItemId'] = self.InvoiceItemId
        if self.RecurringId is not None:
            vals['RecurringId'] = self.RecurringId
        if self.StartDate is not None:
            vals['StartDate'] = self.StartDate
        if self.Status is not None:
            vals['Status'] = self.Status
        return vals

    def _template(self):
        if self.AutoCharge: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EndDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceItemId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.RecurringId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Lead(object):
    global leads
    def __init__(self, values):
        self.values=values
        if 'leads' not in globals():
            leads = []
        if 'AffiliateId' in values.keys():
            self.AffiliateId=values['AffiliateId']
        else:
            self.AffiliateId=None
        if 'ContactID' in values.keys():
            self.ContactID=values['ContactID']
        else:
            self.ContactID=None
        if 'CreatedBy' in values.keys():
            self.CreatedBy=values['CreatedBy']
        else:
            self.CreatedBy=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'EstimatedCloseDate' in values.keys():
            self.EstimatedCloseDate=values['EstimatedCloseDate']
        else:
            self.EstimatedCloseDate=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LastUpdated' in values.keys():
            self.LastUpdated=values['LastUpdated']
        else:
            self.LastUpdated=None
        if 'LastUpdatedBy' in values.keys():
            self.LastUpdatedBy=values['LastUpdatedBy']
        else:
            self.LastUpdatedBy=None
        if 'Leadsource' in values.keys():
            self.Leadsource=values['Leadsource']
        else:
            self.Leadsource=None
        if 'NextActionDate' in values.keys():
            self.NextActionDate=values['NextActionDate']
        else:
            self.NextActionDate=None
        if 'NextActionNotes' in values.keys():
            self.NextActionNotes=values['NextActionNotes']
        else:
            self.NextActionNotes=None
        if 'Objection' in values.keys():
            self.Objection=values['Objection']
        else:
            self.Objection=None
        if 'OpportunityNotes' in values.keys():
            self.OpportunityNotes=values['OpportunityNotes']
        else:
            self.OpportunityNotes=None
        if 'OpportunityTitle' in values.keys():
            self.OpportunityTitle=values['OpportunityTitle']
        else:
            self.OpportunityTitle=None
        if 'ProjectedRevenueHigh' in values.keys():
            self.ProjectedRevenueHigh=values['ProjectedRevenueHigh']
        else:
            self.ProjectedRevenueHigh=None
        if 'ProjectedRevenueLow' in values.keys():
            self.ProjectedRevenueLow=values['ProjectedRevenueLow']
        else:
            self.ProjectedRevenueLow=None
        if 'StageID' in values.keys():
            self.StageID=values['StageID']
        else:
            self.StageID=None
        if 'StatusID' in values.keys():
            self.StatusID=values['StatusID']
        else:
            self.StatusID=None
        if 'UserID' in values.keys():
            self.UserID=values['UserID']
        else:
            self.UserID=None

    def prepare(self):
        vals={}
        if self.AffiliateId is not None:
            vals['AffiliateId'] = self.AffiliateId
        if self.ContactID is not None:
            vals['ContactID'] = self.ContactID
        if self.CreatedBy is not None:
            vals['CreatedBy'] = self.CreatedBy
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.EstimatedCloseDate is not None:
            vals['EstimatedCloseDate'] = self.EstimatedCloseDate
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LastUpdated is not None:
            vals['LastUpdated'] = self.LastUpdated
        if self.LastUpdatedBy is not None:
            vals['LastUpdatedBy'] = self.LastUpdatedBy
        if self.Leadsource is not None:
            vals['Leadsource'] = self.Leadsource
        if self.NextActionDate is not None:
            vals['NextActionDate'] = self.NextActionDate
        if self.NextActionNotes is not None:
            vals['NextActionNotes'] = self.NextActionNotes
        if self.Objection is not None:
            vals['Objection'] = self.Objection
        if self.OpportunityNotes is not None:
            vals['OpportunityNotes'] = self.OpportunityNotes
        if self.OpportunityTitle is not None:
            vals['OpportunityTitle'] = self.OpportunityTitle
        if self.ProjectedRevenueHigh is not None:
            vals['ProjectedRevenueHigh'] = self.ProjectedRevenueHigh
        if self.ProjectedRevenueLow is not None:
            vals['ProjectedRevenueLow'] = self.ProjectedRevenueLow
        if self.StageID is not None:
            vals['StageID'] = self.StageID
        if self.StatusID is not None:
            vals['StatusID'] = self.StatusID
        if self.UserID is not None:
            vals['UserID'] = self.UserID
        return vals

    def _template(self):
        if self.AffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EstimatedCloseDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Leadsource: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NextActionDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NextActionNotes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Objection: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OpportunityNotes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OpportunityTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProjectedRevenueHigh: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProjectedRevenueLow: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StageID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StatusID: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.UserID: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class LeadSource(object):
    global leadsources
    def __init__(self, values):
        self.values=values
        if 'leadsources' not in globals():
            leadsources = []
        if 'CostPerLead' in values.keys():
            self.CostPerLead=values['CostPerLead']
        else:
            self.CostPerLead=None
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'EndDate' in values.keys():
            self.EndDate=values['EndDate']
        else:
            self.EndDate=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LeadSourceCategoryId' in values.keys():
            self.LeadSourceCategoryId=values['LeadSourceCategoryId']
        else:
            self.LeadSourceCategoryId=None
        if 'Medium' in values.keys():
            self.Medium=values['Medium']
        else:
            self.Medium=None
        if 'Message' in values.keys():
            self.Message=values['Message']
        else:
            self.Message=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None
        if 'StartDate' in values.keys():
            self.StartDate=values['StartDate']
        else:
            self.StartDate=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None
        if 'Vendor' in values.keys():
            self.Vendor=values['Vendor']
        else:
            self.Vendor=None

    def prepare(self):
        vals={}
        if self.CostPerLead is not None:
            vals['CostPerLead'] = self.CostPerLead
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.EndDate is not None:
            vals['EndDate'] = self.EndDate
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LeadSourceCategoryId is not None:
            vals['LeadSourceCategoryId'] = self.LeadSourceCategoryId
        if self.Medium is not None:
            vals['Medium'] = self.Medium
        if self.Message is not None:
            vals['Message'] = self.Message
        if self.Name is not None:
            vals['Name'] = self.Name
        if self.StartDate is not None:
            vals['StartDate'] = self.StartDate
        if self.Status is not None:
            vals['Status'] = self.Status
        if self.Vendor is not None:
            vals['Vendor'] = self.Vendor
        return vals

    def _template(self):
        if self.CostPerLead: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EndDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadSourceCategoryId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Medium: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Message: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Vendor: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class LeadSourceCategory(object):
    global leadsourcecategorys
    def __init__(self, values):
        self.values=values
        if 'leadsourcecategorys' not in globals():
            leadsourcecategorys = []
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None

    def prepare(self):
        vals={}
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Name is not None:
            vals['Name'] = self.Name
        return vals

    def _template(self):
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class LeadSourceExpense(object):
    global leadsourceexpenses
    def __init__(self, values):
        self.values=values
        if 'leadsourceexpenses' not in globals():
            leadsourceexpenses = []
        if 'Amount' in values.keys():
            self.Amount=values['Amount']
        else:
            self.Amount=None
        if 'DateIncurred' in values.keys():
            self.DateIncurred=values['DateIncurred']
        else:
            self.DateIncurred=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LeadSourceId' in values.keys():
            self.LeadSourceId=values['LeadSourceId']
        else:
            self.LeadSourceId=None
        if 'LeadSourceRecurringExpenseId' in values.keys():
            self.LeadSourceRecurringExpenseId=values['LeadSourceRecurringExpenseId']
        else:
            self.LeadSourceRecurringExpenseId=None
        if 'Notes' in values.keys():
            self.Notes=values['Notes']
        else:
            self.Notes=None
        if 'Title' in values.keys():
            self.Title=values['Title']
        else:
            self.Title=None

    def prepare(self):
        vals={}
        if self.Amount is not None:
            vals['Amount'] = self.Amount
        if self.DateIncurred is not None:
            vals['DateIncurred'] = self.DateIncurred
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LeadSourceId is not None:
            vals['LeadSourceId'] = self.LeadSourceId
        if self.LeadSourceRecurringExpenseId is not None:
            vals['LeadSourceRecurringExpenseId'] = self.LeadSourceRecurringExpenseId
        if self.Notes is not None:
            vals['Notes'] = self.Notes
        if self.Title is not None:
            vals['Title'] = self.Title
        return vals

    def _template(self):
        if self.Amount: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateIncurred: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadSourceId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadSourceRecurringExpenseId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Notes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class LeadSourceRecurringExpeobjectnse():
    global leadsourcerecurringexpenses
    def __init__(self, values):
        self.values=values
        if 'leadsourcerecurringexpenses' not in globals():
            leadsourcerecurringexpenses = []
        if 'Amount' in values.keys():
            self.Amount=values['Amount']
        else:
            self.Amount=None
        if 'EndDate' in values.keys():
            self.EndDate=values['EndDate']
        else:
            self.EndDate=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LeadSourceId' in values.keys():
            self.LeadSourceId=values['LeadSourceId']
        else:
            self.LeadSourceId=None
        if 'NextExpenseDate' in values.keys():
            self.NextExpenseDate=values['NextExpenseDate']
        else:
            self.NextExpenseDate=None
        if 'Notes' in values.keys():
            self.Notes=values['Notes']
        else:
            self.Notes=None
        if 'StartDate' in values.keys():
            self.StartDate=values['StartDate']
        else:
            self.StartDate=None
        if 'Title' in values.keys():
            self.Title=values['Title']
        else:
            self.Title=None

    def prepare(self):
        vals={}
        if self.Amount is not None:
            vals['Amount'] = self.Amount
        if self.EndDate is not None:
            vals['EndDate'] = self.EndDate
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LeadSourceId is not None:
            vals['LeadSourceId'] = self.LeadSourceId
        if self.NextExpenseDate is not None:
            vals['NextExpenseDate'] = self.NextExpenseDate
        if self.Notes is not None:
            vals['Notes'] = self.Notes
        if self.StartDate is not None:
            vals['StartDate'] = self.StartDate
        if self.Title is not None:
            vals['Title'] = self.Title
        return vals

    def _template(self):
        if self.Amount: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EndDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadSourceId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NextExpenseDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Notes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class MtgLead(object):
    global mtgleads
    def __init__(self, values):
        self.values=values
        if 'mtgleads' not in globals():
            mtgleads = []
        if 'ActualCloseDate' in values.keys():
            self.ActualCloseDate=values['ActualCloseDate']
        else:
            self.ActualCloseDate=None
        if 'ApplicationDate' in values.keys():
            self.ApplicationDate=values['ApplicationDate']
        else:
            self.ApplicationDate=None
        if 'CreditReportDate' in values.keys():
            self.CreditReportDate=values['CreditReportDate']
        else:
            self.CreditReportDate=None
        if 'DateAppraisalDone' in values.keys():
            self.DateAppraisalDone=values['DateAppraisalDone']
        else:
            self.DateAppraisalDone=None
        if 'DateAppraisalOrdered' in values.keys():
            self.DateAppraisalOrdered=values['DateAppraisalOrdered']
        else:
            self.DateAppraisalOrdered=None
        if 'DateAppraisalReceived' in values.keys():
            self.DateAppraisalReceived=values['DateAppraisalReceived']
        else:
            self.DateAppraisalReceived=None
        if 'DateRateLockExpires' in values.keys():
            self.DateRateLockExpires=values['DateRateLockExpires']
        else:
            self.DateRateLockExpires=None
        if 'DateRateLocked' in values.keys():
            self.DateRateLocked=values['DateRateLocked']
        else:
            self.DateRateLocked=None
        if 'DateTitleOrdered' in values.keys():
            self.DateTitleOrdered=values['DateTitleOrdered']
        else:
            self.DateTitleOrdered=None
        if 'DateTitleReceived' in values.keys():
            self.DateTitleReceived=values['DateTitleReceived']
        else:
            self.DateTitleReceived=None
        if 'FundingDate' in values.keys():
            self.FundingDate=values['FundingDate']
        else:
            self.FundingDate=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None

    def prepare(self):
        vals={}
        if self.ActualCloseDate is not None:
            vals['ActualCloseDate'] = self.ActualCloseDate
        if self.ApplicationDate is not None:
            vals['ApplicationDate'] = self.ApplicationDate
        if self.CreditReportDate is not None:
            vals['CreditReportDate'] = self.CreditReportDate
        if self.DateAppraisalDone is not None:
            vals['DateAppraisalDone'] = self.DateAppraisalDone
        if self.DateAppraisalOrdered is not None:
            vals['DateAppraisalOrdered'] = self.DateAppraisalOrdered
        if self.DateAppraisalReceived is not None:
            vals['DateAppraisalReceived'] = self.DateAppraisalReceived
        if self.DateRateLockExpires is not None:
            vals['DateRateLockExpires'] = self.DateRateLockExpires
        if self.DateRateLocked is not None:
            vals['DateRateLocked'] = self.DateRateLocked
        if self.DateTitleOrdered is not None:
            vals['DateTitleOrdered'] = self.DateTitleOrdered
        if self.DateTitleReceived is not None:
            vals['DateTitleReceived'] = self.DateTitleReceived
        if self.FundingDate is not None:
            vals['FundingDate'] = self.FundingDate
        if self.Id is not None:
            vals['Id'] = self.Id
        return vals

    def _template(self):
        if self.ActualCloseDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ApplicationDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreditReportDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateAppraisalDone: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateAppraisalOrdered: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateAppraisalReceived: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateRateLockExpires: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateRateLocked: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateTitleOrdered: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateTitleReceived: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FundingDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class OrderItem(object):
    global orderitems
    def __init__(self, values):
        self.values=values
        if 'orderitems' not in globals():
            orderitems = []
        if 'CPU' in values.keys():
            self.CPU=values['CPU']
        else:
            self.CPU=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'ItemDescription' in values.keys():
            self.ItemDescription=values['ItemDescription']
        else:
            self.ItemDescription=None
        if 'ItemName' in values.keys():
            self.ItemName=values['ItemName']
        else:
            self.ItemName=None
        if 'ItemType' in values.keys():
            self.ItemType=values['ItemType']
        else:
            self.ItemType=None
        if 'Notes' in values.keys():
            self.Notes=values['Notes']
        else:
            self.Notes=None
        if 'OrderId' in values.keys():
            self.OrderId=values['OrderId']
        else:
            self.OrderId=None
        if 'PPU' in values.keys():
            self.PPU=values['PPU']
        else:
            self.PPU=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'Qty' in values.keys():
            self.Qty=values['Qty']
        else:
            self.Qty=None
        if 'SubscriptionPlanId' in values.keys():
            self.SubscriptionPlanId=values['SubscriptionPlanId']
        else:
            self.SubscriptionPlanId=None

    def prepare(self):
        vals={}
        if self.CPU is not None:
            vals['CPU'] = self.CPU
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.ItemDescription is not None:
            vals['ItemDescription'] = self.ItemDescription
        if self.ItemName is not None:
            vals['ItemName'] = self.ItemName
        if self.ItemType is not None:
            vals['ItemType'] = self.ItemType
        if self.Notes is not None:
            vals['Notes'] = self.Notes
        if self.OrderId is not None:
            vals['OrderId'] = self.OrderId
        if self.PPU is not None:
            vals['PPU'] = self.PPU
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.Qty is not None:
            vals['Qty'] = self.Qty
        if self.SubscriptionPlanId is not None:
            vals['SubscriptionPlanId'] = self.SubscriptionPlanId
        return vals

    def _template(self):
        if self.CPU: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ItemDescription: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ItemName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ItemType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Notes: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OrderId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PPU: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Qty: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SubscriptionPlanId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class PayPlan(object):
    global payplans
    def __init__(self, values):
        self.values=values
        if 'payplans' not in globals():
            payplans = []
        if 'AmtDue' in values.keys():
            self.AmtDue=values['AmtDue']
        else:
            self.AmtDue=None
        if 'DateDue' in values.keys():
            self.DateDue=values['DateDue']
        else:
            self.DateDue=None
        if 'FirstPayAmt' in values.keys():
            self.FirstPayAmt=values['FirstPayAmt']
        else:
            self.FirstPayAmt=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'InitDate' in values.keys():
            self.InitDate=values['InitDate']
        else:
            self.InitDate=None
        if 'InvoiceId' in values.keys():
            self.InvoiceId=values['InvoiceId']
        else:
            self.InvoiceId=None
        if 'StartDate' in values.keys():
            self.StartDate=values['StartDate']
        else:
            self.StartDate=None
        if 'Type' in values.keys():
            self.Type=values['Type']
        else:
            self.Type=None

    def prepare(self):
        vals={}
        if self.AmtDue is not None:
            vals['AmtDue'] = self.AmtDue
        if self.DateDue is not None:
            vals['DateDue'] = self.DateDue
        if self.FirstPayAmt is not None:
            vals['FirstPayAmt'] = self.FirstPayAmt
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.InitDate is not None:
            vals['InitDate'] = self.InitDate
        if self.InvoiceId is not None:
            vals['InvoiceId'] = self.InvoiceId
        if self.StartDate is not None:
            vals['StartDate'] = self.StartDate
        if self.Type is not None:
            vals['Type'] = self.Type
        return vals

    def _template(self):
        if self.AmtDue: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateDue: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FirstPayAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InitDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class PayPlanItem(object):
    global payplanitems
    def __init__(self, values):
        self.values=values
        if 'payplanitems' not in globals():
            payplanitems = []
        if 'AmtDue' in values.keys():
            self.AmtDue=values['AmtDue']
        else:
            self.AmtDue=None
        if 'AmtPaid' in values.keys():
            self.AmtPaid=values['AmtPaid']
        else:
            self.AmtPaid=None
        if 'DateDue' in values.keys():
            self.DateDue=values['DateDue']
        else:
            self.DateDue=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'PayPlanId' in values.keys():
            self.PayPlanId=values['PayPlanId']
        else:
            self.PayPlanId=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None

    def prepare(self):
        vals={}
        if self.AmtDue is not None:
            vals['AmtDue'] = self.AmtDue
        if self.AmtPaid is not None:
            vals['AmtPaid'] = self.AmtPaid
        if self.DateDue is not None:
            vals['DateDue'] = self.DateDue
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.PayPlanId is not None:
            vals['PayPlanId'] = self.PayPlanId
        if self.Status is not None:
            vals['Status'] = self.Status
        return vals

    def _template(self):
        if self.AmtDue: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AmtPaid: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateDue: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayPlanId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Payment(object):
    global payments
    def __init__(self, values):
        self.values=values
        if 'payments' not in globals():
            payments = []
        if 'ChargeId' in values.keys():
            self.ChargeId=values['ChargeId']
        else:
            self.ChargeId=None
        if 'Commission' in values.keys():
            self.Commission=values['Commission']
        else:
            self.Commission=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'InvoiceId' in values.keys():
            self.InvoiceId=values['InvoiceId']
        else:
            self.InvoiceId=None
        if 'PayAmt' in values.keys():
            self.PayAmt=values['PayAmt']
        else:
            self.PayAmt=None
        if 'PayDate' in values.keys():
            self.PayDate=values['PayDate']
        else:
            self.PayDate=None
        if 'PayNote' in values.keys():
            self.PayNote=values['PayNote']
        else:
            self.PayNote=None
        if 'PayType' in values.keys():
            self.PayType=values['PayType']
        else:
            self.PayType=None
        if 'RefundId' in values.keys():
            self.RefundId=values['RefundId']
        else:
            self.RefundId=None
        if 'Synced' in values.keys():
            self.Synced=values['Synced']
        else:
            self.Synced=None
        if 'UserId' in values.keys():
            self.UserId=values['UserId']
        else:
            self.UserId=None

    def prepare(self):
        vals={}
        if self.ChargeId is not None:
            vals['ChargeId'] = self.ChargeId
        if self.Commission is not None:
            vals['Commission'] = self.Commission
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.InvoiceId is not None:
            vals['InvoiceId'] = self.InvoiceId
        if self.PayAmt is not None:
            vals['PayAmt'] = self.PayAmt
        if self.PayDate is not None:
            vals['PayDate'] = self.PayDate
        if self.PayNote is not None:
            vals['PayNote'] = self.PayNote
        if self.PayType is not None:
            vals['PayType'] = self.PayType
        if self.RefundId is not None:
            vals['RefundId'] = self.RefundId
        if self.Synced is not None:
            vals['Synced'] = self.Synced
        if self.UserId is not None:
            vals['UserId'] = self.UserId
        return vals

    def _template(self):
        if self.ChargeId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Commission: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InvoiceId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayNote: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PayType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.RefundId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Synced: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.UserId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Product(object):
    global products
    def __init__(self, values):
        self.values=values
        if 'products' not in globals():
            products = []
        if 'BottomHTML' in values.keys():
            self.BottomHTML=values['BottomHTML']
        else:
            self.BottomHTML=None
        if 'CityTaxable' in values.keys():
            self.CityTaxable=values['CityTaxable']
        else:
            self.CityTaxable=None
        if 'CountryTaxable' in values.keys():
            self.CountryTaxable=values['CountryTaxable']
        else:
            self.CountryTaxable=None
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'HideInStore' in values.keys():
            self.HideInStore=values['HideInStore']
        else:
            self.HideInStore=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'InventoryLimit' in values.keys():
            self.InventoryLimit=values['InventoryLimit']
        else:
            self.InventoryLimit=None
        if 'InventoryNotifiee' in values.keys():
            self.InventoryNotifiee=values['InventoryNotifiee']
        else:
            self.InventoryNotifiee=None
        if 'IsPackage' in values.keys():
            self.IsPackage=values['IsPackage']
        else:
            self.IsPackage=None
        if 'LargeImage' in values.keys():
            self.LargeImage=values['LargeImage']
        else:
            self.LargeImage=None
        if 'NeedsDigitalDelivery' in values.keys():
            self.NeedsDigitalDelivery=values['NeedsDigitalDelivery']
        else:
            self.NeedsDigitalDelivery=None
        if 'ProductName' in values.keys():
            self.ProductName=values['ProductName']
        else:
            self.ProductName=None
        if 'ProductPrice' in values.keys():
            self.ProductPrice=values['ProductPrice']
        else:
            self.ProductPrice=None
        if 'Shippable' in values.keys():
            self.Shippable=values['Shippable']
        else:
            self.Shippable=None
        if 'ShippingTime' in values.keys():
            self.ShippingTime=values['ShippingTime']
        else:
            self.ShippingTime=None
        if 'ShortDescription' in values.keys():
            self.ShortDescription=values['ShortDescription']
        else:
            self.ShortDescription=None
        if 'Sku' in values.keys():
            self.Sku=values['Sku']
        else:
            self.Sku=None
        if 'StateTaxable' in values.keys():
            self.StateTaxable=values['StateTaxable']
        else:
            self.StateTaxable=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None
        if 'Taxable' in values.keys():
            self.Taxable=values['Taxable']
        else:
            self.Taxable=None
        if 'TopHTML' in values.keys():
            self.TopHTML=values['TopHTML']
        else:
            self.TopHTML=None
        if 'Weight' in values.keys():
            self.Weight=values['Weight']
        else:
            self.Weight=None

    def prepare(self):
        vals={}
        if self.BottomHTML is not None:
            vals['BottomHTML'] = self.BottomHTML
        if self.CityTaxable is not None:
            vals['CityTaxable'] = self.CityTaxable
        if self.CountryTaxable is not None:
            vals['CountryTaxable'] = self.CountryTaxable
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.HideInStore is not None:
            vals['HideInStore'] = self.HideInStore
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.InventoryLimit is not None:
            vals['InventoryLimit'] = self.InventoryLimit
        if self.InventoryNotifiee is not None:
            vals['InventoryNotifiee'] = self.InventoryNotifiee
        if self.IsPackage is not None:
            vals['IsPackage'] = self.IsPackage
        if self.LargeImage is not None:
            vals['LargeImage'] = self.LargeImage
        if self.NeedsDigitalDelivery is not None:
            vals['NeedsDigitalDelivery'] = self.NeedsDigitalDelivery
        if self.ProductName is not None:
            vals['ProductName'] = self.ProductName
        if self.ProductPrice is not None:
            vals['ProductPrice'] = self.ProductPrice
        if self.Shippable is not None:
            vals['Shippable'] = self.Shippable
        if self.ShippingTime is not None:
            vals['ShippingTime'] = self.ShippingTime
        if self.ShortDescription is not None:
            vals['ShortDescription'] = self.ShortDescription
        if self.Sku is not None:
            vals['Sku'] = self.Sku
        if self.StateTaxable is not None:
            vals['StateTaxable'] = self.StateTaxable
        if self.Status is not None:
            vals['Status'] = self.Status
        if self.Taxable is not None:
            vals['Taxable'] = self.Taxable
        if self.TopHTML is not None:
            vals['TopHTML'] = self.TopHTML
        if self.Weight is not None:
            vals['Weight'] = self.Weight
        return vals

    def _template(self):
        if self.BottomHTML: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CityTaxable: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CountryTaxable: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.HideInStore: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InventoryLimit: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.InventoryNotifiee: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.IsPackage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LargeImage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NeedsDigitalDelivery: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductPrice: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Shippable: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShippingTime: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShortDescription: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Sku: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StateTaxable: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Taxable: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TopHTML: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Weight: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ProductCategory(object):
    global productcategorys
    def __init__(self, values):
        self.values=values
        if 'productcategorys' not in globals():
            productcategorys = []
        if 'CategoryDisplayName' in values.keys():
            self.CategoryDisplayName=values['CategoryDisplayName']
        else:
            self.CategoryDisplayName=None
        if 'CategoryImage' in values.keys():
            self.CategoryImage=values['CategoryImage']
        else:
            self.CategoryImage=None
        if 'CategoryOrder' in values.keys():
            self.CategoryOrder=values['CategoryOrder']
        else:
            self.CategoryOrder=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'ParentId' in values.keys():
            self.ParentId=values['ParentId']
        else:
            self.ParentId=None

    def prepare(self):
        vals={}
        if self.CategoryDisplayName is not None:
            vals['CategoryDisplayName'] = self.CategoryDisplayName
        if self.CategoryImage is not None:
            vals['CategoryImage'] = self.CategoryImage
        if self.CategoryOrder is not None:
            vals['CategoryOrder'] = self.CategoryOrder
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.ParentId is not None:
            vals['ParentId'] = self.ParentId
        return vals

    def _template(self):
        if self.CategoryDisplayName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CategoryImage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CategoryOrder: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ParentId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ProductCategoryAssign(object):
    global productcategoryassigns
    def __init__(self, values):
        self.values=values
        if 'productcategoryassigns' not in globals():
            productcategoryassigns = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'ProductCategoryId' in values.keys():
            self.ProductCategoryId=values['ProductCategoryId']
        else:
            self.ProductCategoryId=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.ProductCategoryId is not None:
            vals['ProductCategoryId'] = self.ProductCategoryId
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductCategoryId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ProductInterest(object):
    global productinterests
    def __init__(self, values):
        self.values=values
        if 'productinterests' not in globals():
            productinterests = []
        if 'DiscountPercent' in values.keys():
            self.DiscountPercent=values['DiscountPercent']
        else:
            self.DiscountPercent=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'ObjType' in values.keys():
            self.ObjType=values['ObjType']
        else:
            self.ObjType=None
        if 'ObjectId' in values.keys():
            self.ObjectId=values['ObjectId']
        else:
            self.ObjectId=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'ProductType' in values.keys():
            self.ProductType=values['ProductType']
        else:
            self.ProductType=None
        if 'Qty' in values.keys():
            self.Qty=values['Qty']
        else:
            self.Qty=None

    def prepare(self):
        vals={}
        if self.DiscountPercent is not None:
            vals['DiscountPercent'] = self.DiscountPercent
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.ObjType is not None:
            vals['ObjType'] = self.ObjType
        if self.ObjectId is not None:
            vals['ObjectId'] = self.ObjectId
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.ProductType is not None:
            vals['ProductType'] = self.ProductType
        if self.Qty is not None:
            vals['Qty'] = self.Qty
        return vals

    def _template(self):
        if self.DiscountPercent: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ObjType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ObjectId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Qty: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ProductInterestBundle(object):
    global productinterestbundles
    def __init__(self, values):
        self.values=values
        if 'productinterestbundles' not in globals():
            productinterestbundles = []
        if 'BundleName' in values.keys():
            self.BundleName=values['BundleName']
        else:
            self.BundleName=None
        if 'Description' in values.keys():
            self.Description=values['Description']
        else:
            self.Description=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None

    def prepare(self):
        vals={}
        if self.BundleName is not None:
            vals['BundleName'] = self.BundleName
        if self.Description is not None:
            vals['Description'] = self.Description
        if self.Id is not None:
            vals['Id'] = self.Id
        return vals

    def _template(self):
        if self.BundleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Description: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ProductOptValue(object):
    global productoptvalues
    def __init__(self, values):
        self.values=values
        if 'productoptvalues' not in globals():
            productoptvalues = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'IsDefault' in values.keys():
            self.IsDefault=values['IsDefault']
        else:
            self.IsDefault=None
        if 'Label' in values.keys():
            self.Label=values['Label']
        else:
            self.Label=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None
        if 'OptionIndex' in values.keys():
            self.OptionIndex=values['OptionIndex']
        else:
            self.OptionIndex=None
        if 'PriceAdjustment' in values.keys():
            self.PriceAdjustment=values['PriceAdjustment']
        else:
            self.PriceAdjustment=None
        if 'ProductOptionId' in values.keys():
            self.ProductOptionId=values['ProductOptionId']
        else:
            self.ProductOptionId=None
        if 'Sku' in values.keys():
            self.Sku=values['Sku']
        else:
            self.Sku=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.IsDefault is not None:
            vals['IsDefault'] = self.IsDefault
        if self.Label is not None:
            vals['Label'] = self.Label
        if self.Name is not None:
            vals['Name'] = self.Name
        if self.OptionIndex is not None:
            vals['OptionIndex'] = self.OptionIndex
        if self.PriceAdjustment is not None:
            vals['PriceAdjustment'] = self.PriceAdjustment
        if self.ProductOptionId is not None:
            vals['ProductOptionId'] = self.ProductOptionId
        if self.Sku is not None:
            vals['Sku'] = self.Sku
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.IsDefault: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Label: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OptionIndex: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PriceAdjustment: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductOptionId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Sku: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class ProductOption(object):
    global productoptions
    def __init__(self, values):
        self.values=values
        if 'productoptions' not in globals():
            productoptions = []
        if 'AllowSpaces' in values.keys():
            self.AllowSpaces=values['AllowSpaces']
        else:
            self.AllowSpaces=None
        if 'CanContain' in values.keys():
            self.CanContain=values['CanContain']
        else:
            self.CanContain=None
        if 'CanEndWith' in values.keys():
            self.CanEndWith=values['CanEndWith']
        else:
            self.CanEndWith=None
        if 'CanStartWith' in values.keys():
            self.CanStartWith=values['CanStartWith']
        else:
            self.CanStartWith=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'IsRequired' in values.keys():
            self.IsRequired=values['IsRequired']
        else:
            self.IsRequired=None
        if 'Label' in values.keys():
            self.Label=values['Label']
        else:
            self.Label=None
        if 'MaxChars' in values.keys():
            self.MaxChars=values['MaxChars']
        else:
            self.MaxChars=None
        if 'MinChars' in values.keys():
            self.MinChars=values['MinChars']
        else:
            self.MinChars=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None
        if 'OptionType' in values.keys():
            self.OptionType=values['OptionType']
        else:
            self.OptionType=None
        if 'Order' in values.keys():
            self.Order=values['Order']
        else:
            self.Order=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'TextMessage' in values.keys():
            self.TextMessage=values['TextMessage']
        else:
            self.TextMessage=None

    def prepare(self):
        vals={}
        if self.AllowSpaces is not None:
            vals['AllowSpaces'] = self.AllowSpaces
        if self.CanContain is not None:
            vals['CanContain'] = self.CanContain
        if self.CanEndWith is not None:
            vals['CanEndWith'] = self.CanEndWith
        if self.CanStartWith is not None:
            vals['CanStartWith'] = self.CanStartWith
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.IsRequired is not None:
            vals['IsRequired'] = self.IsRequired
        if self.Label is not None:
            vals['Label'] = self.Label
        if self.MaxChars is not None:
            vals['MaxChars'] = self.MaxChars
        if self.MinChars is not None:
            vals['MinChars'] = self.MinChars
        if self.Name is not None:
            vals['Name'] = self.Name
        if self.OptionType is not None:
            vals['OptionType'] = self.OptionType
        if self.Order is not None:
            vals['Order'] = self.Order
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.TextMessage is not None:
            vals['TextMessage'] = self.TextMessage
        return vals

    def _template(self):
        if self.AllowSpaces: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CanContain: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CanEndWith: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CanStartWith: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.IsRequired: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Label: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MaxChars: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MinChars: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OptionType: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Order: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TextMessage: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class RecurringOrder(object):
    global recurringorders
    def __init__(self, values):
        self.values=values
        if 'recurringorders' not in globals():
            recurringorders = []
        if 'AffiliateId' in values.keys():
            self.AffiliateId=values['AffiliateId']
        else:
            self.AffiliateId=None
        if 'AutoCharge' in values.keys():
            self.AutoCharge=values['AutoCharge']
        else:
            self.AutoCharge=None
        if 'BillingAmt' in values.keys():
            self.BillingAmt=values['BillingAmt']
        else:
            self.BillingAmt=None
        if 'BillingCycle' in values.keys():
            self.BillingCycle=values['BillingCycle']
        else:
            self.BillingCycle=None
        if 'CC1' in values.keys():
            self.CC1=values['CC1']
        else:
            self.CC1=None
        if 'CC2' in values.keys():
            self.CC2=values['CC2']
        else:
            self.CC2=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'EndDate' in values.keys():
            self.EndDate=values['EndDate']
        else:
            self.EndDate=None
        if 'Frequency' in values.keys():
            self.Frequency=values['Frequency']
        else:
            self.Frequency=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LastBillDate' in values.keys():
            self.LastBillDate=values['LastBillDate']
        else:
            self.LastBillDate=None
        if 'LeadAffiliateId' in values.keys():
            self.LeadAffiliateId=values['LeadAffiliateId']
        else:
            self.LeadAffiliateId=None
        if 'MaxRetry' in values.keys():
            self.MaxRetry=values['MaxRetry']
        else:
            self.MaxRetry=None
        if 'MerchantAccountId' in values.keys():
            self.MerchantAccountId=values['MerchantAccountId']
        else:
            self.MerchantAccountId=None
        if 'NextBillDate' in values.keys():
            self.NextBillDate=values['NextBillDate']
        else:
            self.NextBillDate=None
        if 'NumDaysBetweenRetry' in values.keys():
            self.NumDaysBetweenRetry=values['NumDaysBetweenRetry']
        else:
            self.NumDaysBetweenRetry=None
        if 'OriginatingOrderId' in values.keys():
            self.OriginatingOrderId=values['OriginatingOrderId']
        else:
            self.OriginatingOrderId=None
        if 'PaidThruDate' in values.keys():
            self.PaidThruDate=values['PaidThruDate']
        else:
            self.PaidThruDate=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'ProgramId' in values.keys():
            self.ProgramId=values['ProgramId']
        else:
            self.ProgramId=None
        if 'PromoCode' in values.keys():
            self.PromoCode=values['PromoCode']
        else:
            self.PromoCode=None
        if 'Qty' in values.keys():
            self.Qty=values['Qty']
        else:
            self.Qty=None
        if 'ReasonStopped' in values.keys():
            self.ReasonStopped=values['ReasonStopped']
        else:
            self.ReasonStopped=None
        if 'ShippingOptionId' in values.keys():
            self.ShippingOptionId=values['ShippingOptionId']
        else:
            self.ShippingOptionId=None
        if 'StartDate' in values.keys():
            self.StartDate=values['StartDate']
        else:
            self.StartDate=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None
        if 'SubscriptionPlanId' in values.keys():
            self.SubscriptionPlanId=values['SubscriptionPlanId']
        else:
            self.SubscriptionPlanId=None

    def prepare(self):
        vals={}
        if self.AffiliateId is not None:
            vals['AffiliateId'] = self.AffiliateId
        if self.AutoCharge is not None:
            vals['AutoCharge'] = self.AutoCharge
        if self.BillingAmt is not None:
            vals['BillingAmt'] = self.BillingAmt
        if self.BillingCycle is not None:
            vals['BillingCycle'] = self.BillingCycle
        if self.CC1 is not None:
            vals['CC1'] = self.CC1
        if self.CC2 is not None:
            vals['CC2'] = self.CC2
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.EndDate is not None:
            vals['EndDate'] = self.EndDate
        if self.Frequency is not None:
            vals['Frequency'] = self.Frequency
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LastBillDate is not None:
            vals['LastBillDate'] = self.LastBillDate
        if self.LeadAffiliateId is not None:
            vals['LeadAffiliateId'] = self.LeadAffiliateId
        if self.MaxRetry is not None:
            vals['MaxRetry'] = self.MaxRetry
        if self.MerchantAccountId is not None:
            vals['MerchantAccountId'] = self.MerchantAccountId
        if self.NextBillDate is not None:
            vals['NextBillDate'] = self.NextBillDate
        if self.NumDaysBetweenRetry is not None:
            vals['NumDaysBetweenRetry'] = self.NumDaysBetweenRetry
        if self.OriginatingOrderId is not None:
            vals['OriginatingOrderId'] = self.OriginatingOrderId
        if self.PaidThruDate is not None:
            vals['PaidThruDate'] = self.PaidThruDate
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.ProgramId is not None:
            vals['ProgramId'] = self.ProgramId
        if self.PromoCode is not None:
            vals['PromoCode'] = self.PromoCode
        if self.Qty is not None:
            vals['Qty'] = self.Qty
        if self.ReasonStopped is not None:
            vals['ReasonStopped'] = self.ReasonStopped
        if self.ShippingOptionId is not None:
            vals['ShippingOptionId'] = self.ShippingOptionId
        if self.StartDate is not None:
            vals['StartDate'] = self.StartDate
        if self.Status is not None:
            vals['Status'] = self.Status
        if self.SubscriptionPlanId is not None:
            vals['SubscriptionPlanId'] = self.SubscriptionPlanId
        return vals

    def _template(self):
        if self.AffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AutoCharge: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillingAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillingCycle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CC1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CC2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EndDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Frequency: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastBillDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadAffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MaxRetry: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MerchantAccountId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NextBillDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NumDaysBetweenRetry: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OriginatingOrderId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PaidThruDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProgramId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PromoCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Qty: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ReasonStopped: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShippingOptionId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SubscriptionPlanId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class RecurringOrderWithContaobjectct():
    global recurringorderwithcontacts
    def __init__(self, values):
        self.values=values
        if 'recurringorderwithcontacts' not in globals():
            recurringorderwithcontacts = []
        if 'AffiliateId' in values.keys():
            self.AffiliateId=values['AffiliateId']
        else:
            self.AffiliateId=None
        if 'AutoCharge' in values.keys():
            self.AutoCharge=values['AutoCharge']
        else:
            self.AutoCharge=None
        if 'BillingAmt' in values.keys():
            self.BillingAmt=values['BillingAmt']
        else:
            self.BillingAmt=None
        if 'BillingCycle' in values.keys():
            self.BillingCycle=values['BillingCycle']
        else:
            self.BillingCycle=None
        if 'CC1' in values.keys():
            self.CC1=values['CC1']
        else:
            self.CC1=None
        if 'CC2' in values.keys():
            self.CC2=values['CC2']
        else:
            self.CC2=None
        if 'City' in values.keys():
            self.City=values['City']
        else:
            self.City=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'Country' in values.keys():
            self.Country=values['Country']
        else:
            self.Country=None
        if 'Email' in values.keys():
            self.Email=values['Email']
        else:
            self.Email=None
        if 'EmailAddress2' in values.keys():
            self.EmailAddress2=values['EmailAddress2']
        else:
            self.EmailAddress2=None
        if 'EmailAddress3' in values.keys():
            self.EmailAddress3=values['EmailAddress3']
        else:
            self.EmailAddress3=None
        if 'EndDate' in values.keys():
            self.EndDate=values['EndDate']
        else:
            self.EndDate=None
        if 'FirstName' in values.keys():
            self.FirstName=values['FirstName']
        else:
            self.FirstName=None
        if 'Frequency' in values.keys():
            self.Frequency=values['Frequency']
        else:
            self.Frequency=None
        if 'HTMLSignature' in values.keys():
            self.HTMLSignature=values['HTMLSignature']
        else:
            self.HTMLSignature=None
        if 'LastBillDate' in values.keys():
            self.LastBillDate=values['LastBillDate']
        else:
            self.LastBillDate=None
        if 'LastName' in values.keys():
            self.LastName=values['LastName']
        else:
            self.LastName=None
        if 'LeadAffiliateId' in values.keys():
            self.LeadAffiliateId=values['LeadAffiliateId']
        else:
            self.LeadAffiliateId=None
        if 'MaxRetry' in values.keys():
            self.MaxRetry=values['MaxRetry']
        else:
            self.MaxRetry=None
        if 'MerchantAccountId' in values.keys():
            self.MerchantAccountId=values['MerchantAccountId']
        else:
            self.MerchantAccountId=None
        if 'MiddleName' in values.keys():
            self.MiddleName=values['MiddleName']
        else:
            self.MiddleName=None
        if 'NextBillDate' in values.keys():
            self.NextBillDate=values['NextBillDate']
        else:
            self.NextBillDate=None
        if 'Nickname' in values.keys():
            self.Nickname=values['Nickname']
        else:
            self.Nickname=None
        if 'NumDaysBetweenRetry' in values.keys():
            self.NumDaysBetweenRetry=values['NumDaysBetweenRetry']
        else:
            self.NumDaysBetweenRetry=None
        if 'PaidThruDate' in values.keys():
            self.PaidThruDate=values['PaidThruDate']
        else:
            self.PaidThruDate=None
        if 'Phone1' in values.keys():
            self.Phone1=values['Phone1']
        else:
            self.Phone1=None
        if 'Phone1Ext' in values.keys():
            self.Phone1Ext=values['Phone1Ext']
        else:
            self.Phone1Ext=None
        if 'Phone1Type' in values.keys():
            self.Phone1Type=values['Phone1Type']
        else:
            self.Phone1Type=None
        if 'Phone2' in values.keys():
            self.Phone2=values['Phone2']
        else:
            self.Phone2=None
        if 'Phone2Ext' in values.keys():
            self.Phone2Ext=values['Phone2Ext']
        else:
            self.Phone2Ext=None
        if 'Phone2Type' in values.keys():
            self.Phone2Type=values['Phone2Type']
        else:
            self.Phone2Type=None
        if 'PostalCode' in values.keys():
            self.PostalCode=values['PostalCode']
        else:
            self.PostalCode=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'ProgramId' in values.keys():
            self.ProgramId=values['ProgramId']
        else:
            self.ProgramId=None
        if 'PromoCode' in values.keys():
            self.PromoCode=values['PromoCode']
        else:
            self.PromoCode=None
        if 'Qty' in values.keys():
            self.Qty=values['Qty']
        else:
            self.Qty=None
        if 'ReasonStopped' in values.keys():
            self.ReasonStopped=values['ReasonStopped']
        else:
            self.ReasonStopped=None
        if 'RecurringOrderId' in values.keys():
            self.RecurringOrderId=values['RecurringOrderId']
        else:
            self.RecurringOrderId=None
        if 'ShippingOptionId' in values.keys():
            self.ShippingOptionId=values['ShippingOptionId']
        else:
            self.ShippingOptionId=None
        if 'Signature' in values.keys():
            self.Signature=values['Signature']
        else:
            self.Signature=None
        if 'SpouseName' in values.keys():
            self.SpouseName=values['SpouseName']
        else:
            self.SpouseName=None
        if 'StartDate' in values.keys():
            self.StartDate=values['StartDate']
        else:
            self.StartDate=None
        if 'State' in values.keys():
            self.State=values['State']
        else:
            self.State=None
        if 'Status' in values.keys():
            self.Status=values['Status']
        else:
            self.Status=None
        if 'StreetAddress1' in values.keys():
            self.StreetAddress1=values['StreetAddress1']
        else:
            self.StreetAddress1=None
        if 'StreetAddress2' in values.keys():
            self.StreetAddress2=values['StreetAddress2']
        else:
            self.StreetAddress2=None
        if 'SubscriptionPlanId' in values.keys():
            self.SubscriptionPlanId=values['SubscriptionPlanId']
        else:
            self.SubscriptionPlanId=None
        if 'Suffix' in values.keys():
            self.Suffix=values['Suffix']
        else:
            self.Suffix=None
        if 'Title' in values.keys():
            self.Title=values['Title']
        else:
            self.Title=None
        if 'ZipFour1' in values.keys():
            self.ZipFour1=values['ZipFour1']
        else:
            self.ZipFour1=None

    def prepare(self):
        vals={}
        if self.AffiliateId is not None:
            vals['AffiliateId'] = self.AffiliateId
        if self.AutoCharge is not None:
            vals['AutoCharge'] = self.AutoCharge
        if self.BillingAmt is not None:
            vals['BillingAmt'] = self.BillingAmt
        if self.BillingCycle is not None:
            vals['BillingCycle'] = self.BillingCycle
        if self.CC1 is not None:
            vals['CC1'] = self.CC1
        if self.CC2 is not None:
            vals['CC2'] = self.CC2
        if self.City is not None:
            vals['City'] = self.City
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.Country is not None:
            vals['Country'] = self.Country
        if self.Email is not None:
            vals['Email'] = self.Email
        if self.EmailAddress2 is not None:
            vals['EmailAddress2'] = self.EmailAddress2
        if self.EmailAddress3 is not None:
            vals['EmailAddress3'] = self.EmailAddress3
        if self.EndDate is not None:
            vals['EndDate'] = self.EndDate
        if self.FirstName is not None:
            vals['FirstName'] = self.FirstName
        if self.Frequency is not None:
            vals['Frequency'] = self.Frequency
        if self.HTMLSignature is not None:
            vals['HTMLSignature'] = self.HTMLSignature
        if self.LastBillDate is not None:
            vals['LastBillDate'] = self.LastBillDate
        if self.LastName is not None:
            vals['LastName'] = self.LastName
        if self.LeadAffiliateId is not None:
            vals['LeadAffiliateId'] = self.LeadAffiliateId
        if self.MaxRetry is not None:
            vals['MaxRetry'] = self.MaxRetry
        if self.MerchantAccountId is not None:
            vals['MerchantAccountId'] = self.MerchantAccountId
        if self.MiddleName is not None:
            vals['MiddleName'] = self.MiddleName
        if self.NextBillDate is not None:
            vals['NextBillDate'] = self.NextBillDate
        if self.Nickname is not None:
            vals['Nickname'] = self.Nickname
        if self.NumDaysBetweenRetry is not None:
            vals['NumDaysBetweenRetry'] = self.NumDaysBetweenRetry
        if self.PaidThruDate is not None:
            vals['PaidThruDate'] = self.PaidThruDate
        if self.Phone1 is not None:
            vals['Phone1'] = self.Phone1
        if self.Phone1Ext is not None:
            vals['Phone1Ext'] = self.Phone1Ext
        if self.Phone1Type is not None:
            vals['Phone1Type'] = self.Phone1Type
        if self.Phone2 is not None:
            vals['Phone2'] = self.Phone2
        if self.Phone2Ext is not None:
            vals['Phone2Ext'] = self.Phone2Ext
        if self.Phone2Type is not None:
            vals['Phone2Type'] = self.Phone2Type
        if self.PostalCode is not None:
            vals['PostalCode'] = self.PostalCode
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.ProgramId is not None:
            vals['ProgramId'] = self.ProgramId
        if self.PromoCode is not None:
            vals['PromoCode'] = self.PromoCode
        if self.Qty is not None:
            vals['Qty'] = self.Qty
        if self.ReasonStopped is not None:
            vals['ReasonStopped'] = self.ReasonStopped
        if self.RecurringOrderId is not None:
            vals['RecurringOrderId'] = self.RecurringOrderId
        if self.ShippingOptionId is not None:
            vals['ShippingOptionId'] = self.ShippingOptionId
        if self.Signature is not None:
            vals['Signature'] = self.Signature
        if self.SpouseName is not None:
            vals['SpouseName'] = self.SpouseName
        if self.StartDate is not None:
            vals['StartDate'] = self.StartDate
        if self.State is not None:
            vals['State'] = self.State
        if self.Status is not None:
            vals['Status'] = self.Status
        if self.StreetAddress1 is not None:
            vals['StreetAddress1'] = self.StreetAddress1
        if self.StreetAddress2 is not None:
            vals['StreetAddress2'] = self.StreetAddress2
        if self.SubscriptionPlanId is not None:
            vals['SubscriptionPlanId'] = self.SubscriptionPlanId
        if self.Suffix is not None:
            vals['Suffix'] = self.Suffix
        if self.Title is not None:
            vals['Title'] = self.Title
        if self.ZipFour1 is not None:
            vals['ZipFour1'] = self.ZipFour1
        return vals

    def _template(self):
        if self.AffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.AutoCharge: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillingAmt: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.BillingCycle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CC1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CC2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.City: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Country: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Email: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EndDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Frequency: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.HTMLSignature: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastBillDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LeadAffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MaxRetry: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MerchantAccountId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MiddleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NextBillDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Nickname: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.NumDaysBetweenRetry: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PaidThruDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProgramId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PromoCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Qty: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ReasonStopped: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.RecurringOrderId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ShippingOptionId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Signature: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SpouseName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StartDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Status: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SubscriptionPlanId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Suffix: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour1: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Referral(object):
    global referrals
    def __init__(self, values):
        self.values=values
        if 'referrals' not in globals():
            referrals = []
        if 'AffiliateId' in values.keys():
            self.AffiliateId=values['AffiliateId']
        else:
            self.AffiliateId=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'DateExpires' in values.keys():
            self.DateExpires=values['DateExpires']
        else:
            self.DateExpires=None
        if 'DateSet' in values.keys():
            self.DateSet=values['DateSet']
        else:
            self.DateSet=None
        if 'IPAddress' in values.keys():
            self.IPAddress=values['IPAddress']
        else:
            self.IPAddress=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Info' in values.keys():
            self.Info=values['Info']
        else:
            self.Info=None
        if 'Source' in values.keys():
            self.Source=values['Source']
        else:
            self.Source=None
        if 'Type' in values.keys():
            self.Type=values['Type']
        else:
            self.Type=None

    def prepare(self):
        vals={}
        if self.AffiliateId is not None:
            vals['AffiliateId'] = self.AffiliateId
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.DateExpires is not None:
            vals['DateExpires'] = self.DateExpires
        if self.DateSet is not None:
            vals['DateSet'] = self.DateSet
        if self.IPAddress is not None:
            vals['IPAddress'] = self.IPAddress
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Info is not None:
            vals['Info'] = self.Info
        if self.Source is not None:
            vals['Source'] = self.Source
        if self.Type is not None:
            vals['Type'] = self.Type
        return vals

    def _template(self):
        if self.AffiliateId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateExpires: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateSet: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.IPAddress: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Info: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Source: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class SavedFilter(object):
    global savedfilters
    def __init__(self, values):
        self.values=values
        if 'savedfilters' not in globals():
            savedfilters = []
        if 'FilterName' in values.keys():
            self.FilterName=values['FilterName']
        else:
            self.FilterName=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'ReportStoredName' in values.keys():
            self.ReportStoredName=values['ReportStoredName']
        else:
            self.ReportStoredName=None
        if 'UserId' in values.keys():
            self.UserId=values['UserId']
        else:
            self.UserId=None

    def prepare(self):
        vals={}
        if self.FilterName is not None:
            vals['FilterName'] = self.FilterName
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.ReportStoredName is not None:
            vals['ReportStoredName'] = self.ReportStoredName
        if self.UserId is not None:
            vals['UserId'] = self.UserId
        return vals

    def _template(self):
        if self.FilterName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ReportStoredName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.UserId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Stage(object):
    global stages
    def __init__(self, values):
        self.values=values
        if 'stages' not in globals():
            stages = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'StageName' in values.keys():
            self.StageName=values['StageName']
        else:
            self.StageName=None
        if 'StageOrder' in values.keys():
            self.StageOrder=values['StageOrder']
        else:
            self.StageOrder=None
        if 'TargetNumDays' in values.keys():
            self.TargetNumDays=values['TargetNumDays']
        else:
            self.TargetNumDays=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.StageName is not None:
            vals['StageName'] = self.StageName
        if self.StageOrder is not None:
            vals['StageOrder'] = self.StageOrder
        if self.TargetNumDays is not None:
            vals['TargetNumDays'] = self.TargetNumDays
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StageName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StageOrder: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TargetNumDays: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class StageMove(object):
    global stagemoves
    def __init__(self, values):
        self.values=values
        if 'stagemoves' not in globals():
            stagemoves = []
        if 'CreatedBy' in values.keys():
            self.CreatedBy=values['CreatedBy']
        else:
            self.CreatedBy=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'MoveDate' in values.keys():
            self.MoveDate=values['MoveDate']
        else:
            self.MoveDate=None
        if 'MoveFromStage' in values.keys():
            self.MoveFromStage=values['MoveFromStage']
        else:
            self.MoveFromStage=None
        if 'MoveToStage' in values.keys():
            self.MoveToStage=values['MoveToStage']
        else:
            self.MoveToStage=None
        if 'OpportunityId' in values.keys():
            self.OpportunityId=values['OpportunityId']
        else:
            self.OpportunityId=None
        if 'PrevStageMoveDate' in values.keys():
            self.PrevStageMoveDate=values['PrevStageMoveDate']
        else:
            self.PrevStageMoveDate=None
        if 'UserId' in values.keys():
            self.UserId=values['UserId']
        else:
            self.UserId=None

    def prepare(self):
        vals={}
        if self.CreatedBy is not None:
            vals['CreatedBy'] = self.CreatedBy
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.MoveDate is not None:
            vals['MoveDate'] = self.MoveDate
        if self.MoveFromStage is not None:
            vals['MoveFromStage'] = self.MoveFromStage
        if self.MoveToStage is not None:
            vals['MoveToStage'] = self.MoveToStage
        if self.OpportunityId is not None:
            vals['OpportunityId'] = self.OpportunityId
        if self.PrevStageMoveDate is not None:
            vals['PrevStageMoveDate'] = self.PrevStageMoveDate
        if self.UserId is not None:
            vals['UserId'] = self.UserId
        return vals

    def _template(self):
        if self.CreatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MoveDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MoveFromStage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MoveToStage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OpportunityId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PrevStageMoveDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.UserId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Status(object):
    global statuss
    def __init__(self, values):
        self.values=values
        if 'statuss' not in globals():
            statuss = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'StatusName' in values.keys():
            self.StatusName=values['StatusName']
        else:
            self.StatusName=None
        if 'StatusOrder' in values.keys():
            self.StatusOrder=values['StatusOrder']
        else:
            self.StatusOrder=None
        if 'TargetNumDays' in values.keys():
            self.TargetNumDays=values['TargetNumDays']
        else:
            self.TargetNumDays=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.StatusName is not None:
            vals['StatusName'] = self.StatusName
        if self.StatusOrder is not None:
            vals['StatusOrder'] = self.StatusOrder
        if self.TargetNumDays is not None:
            vals['TargetNumDays'] = self.TargetNumDays
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StatusName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StatusOrder: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TargetNumDays: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class SubscriptionPlan(object):
    global subscriptionplans
    def __init__(self, values):
        self.values=values
        if 'subscriptionplans' not in globals():
            subscriptionplans = []
        if 'Active' in values.keys():
            self.Active=values['Active']
        else:
            self.Active=None
        if 'Cycle' in values.keys():
            self.Cycle=values['Cycle']
        else:
            self.Cycle=None
        if 'Frequency' in values.keys():
            self.Frequency=values['Frequency']
        else:
            self.Frequency=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'PlanPrice' in values.keys():
            self.PlanPrice=values['PlanPrice']
        else:
            self.PlanPrice=None
        if 'PreAuthorizeAmount' in values.keys():
            self.PreAuthorizeAmount=values['PreAuthorizeAmount']
        else:
            self.PreAuthorizeAmount=None
        if 'ProductId' in values.keys():
            self.ProductId=values['ProductId']
        else:
            self.ProductId=None
        if 'Prorate' in values.keys():
            self.Prorate=values['Prorate']
        else:
            self.Prorate=None

    def prepare(self):
        vals={}
        if self.Active is not None:
            vals['Active'] = self.Active
        if self.Cycle is not None:
            vals['Cycle'] = self.Cycle
        if self.Frequency is not None:
            vals['Frequency'] = self.Frequency
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.PlanPrice is not None:
            vals['PlanPrice'] = self.PlanPrice
        if self.PreAuthorizeAmount is not None:
            vals['PreAuthorizeAmount'] = self.PreAuthorizeAmount
        if self.ProductId is not None:
            vals['ProductId'] = self.ProductId
        if self.Prorate is not None:
            vals['Prorate'] = self.Prorate
        return vals

    def _template(self):
        if self.Active: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Cycle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Frequency: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PlanPrice: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PreAuthorizeAmount: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ProductId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Prorate: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Template(object):
    global templates
    def __init__(self, values):
        self.values=values
        if 'templates' not in globals():
            templates = []
        if 'Categories' in values.keys():
            self.Categories=values['Categories']
        else:
            self.Categories=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'PieceTitle' in values.keys():
            self.PieceTitle=values['PieceTitle']
        else:
            self.PieceTitle=None
        if 'PieceType' in values.keys():
            self.PieceType=values['PieceType']
        else:
            self.PieceType=None

    def prepare(self):
        vals={}
        if self.Categories is not None:
            vals['Categories'] = self.Categories
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.PieceTitle is not None:
            vals['PieceTitle'] = self.PieceTitle
        if self.PieceType is not None:
            vals['PieceType'] = self.PieceType
        return vals

    def _template(self):
        if self.Categories: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PieceTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PieceType: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class Ticket(object):
    global tickets
    def __init__(self, values):
        self.values=values
        if 'tickets' not in globals():
            tickets = []
        if 'CloseDate' in values.keys():
            self.CloseDate=values['CloseDate']
        else:
            self.CloseDate=None
        if 'ContactId' in values.keys():
            self.ContactId=values['ContactId']
        else:
            self.ContactId=None
        if 'CreatedBy' in values.keys():
            self.CreatedBy=values['CreatedBy']
        else:
            self.CreatedBy=None
        if 'DateCreated' in values.keys():
            self.DateCreated=values['DateCreated']
        else:
            self.DateCreated=None
        if 'DateInStage' in values.keys():
            self.DateInStage=values['DateInStage']
        else:
            self.DateInStage=None
        if 'DevId' in values.keys():
            self.DevId=values['DevId']
        else:
            self.DevId=None
        if 'FolowUpDate' in values.keys():
            self.FolowUpDate=values['FolowUpDate']
        else:
            self.FolowUpDate=None
        if 'HasCustomerCalled' in values.keys():
            self.HasCustomerCalled=values['HasCustomerCalled']
        else:
            self.HasCustomerCalled=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'IssueId' in values.keys():
            self.IssueId=values['IssueId']
        else:
            self.IssueId=None
        if 'LastUpdated' in values.keys():
            self.LastUpdated=values['LastUpdated']
        else:
            self.LastUpdated=None
        if 'LastUpdatedBy' in values.keys():
            self.LastUpdatedBy=values['LastUpdatedBy']
        else:
            self.LastUpdatedBy=None
        if 'Ordering' in values.keys():
            self.Ordering=values['Ordering']
        else:
            self.Ordering=None
        if 'Priority' in values.keys():
            self.Priority=values['Priority']
        else:
            self.Priority=None
        if 'Stage' in values.keys():
            self.Stage=values['Stage']
        else:
            self.Stage=None
        if 'Summary' in values.keys():
            self.Summary=values['Summary']
        else:
            self.Summary=None
        if 'TargetCompletionDate' in values.keys():
            self.TargetCompletionDate=values['TargetCompletionDate']
        else:
            self.TargetCompletionDate=None
        if 'TicketApplication' in values.keys():
            self.TicketApplication=values['TicketApplication']
        else:
            self.TicketApplication=None
        if 'TicketCategory' in values.keys():
            self.TicketCategory=values['TicketCategory']
        else:
            self.TicketCategory=None
        if 'TicketTitle' in values.keys():
            self.TicketTitle=values['TicketTitle']
        else:
            self.TicketTitle=None
        if 'TicketTypeId' in values.keys():
            self.TicketTypeId=values['TicketTypeId']
        else:
            self.TicketTypeId=None
        if 'TimeSpent' in values.keys():
            self.TimeSpent=values['TimeSpent']
        else:
            self.TimeSpent=None
        if 'UserId' in values.keys():
            self.UserId=values['UserId']
        else:
            self.UserId=None

    def prepare(self):
        vals={}
        if self.CloseDate is not None:
            vals['CloseDate'] = self.CloseDate
        if self.ContactId is not None:
            vals['ContactId'] = self.ContactId
        if self.CreatedBy is not None:
            vals['CreatedBy'] = self.CreatedBy
        if self.DateCreated is not None:
            vals['DateCreated'] = self.DateCreated
        if self.DateInStage is not None:
            vals['DateInStage'] = self.DateInStage
        if self.DevId is not None:
            vals['DevId'] = self.DevId
        if self.FolowUpDate is not None:
            vals['FolowUpDate'] = self.FolowUpDate
        if self.HasCustomerCalled is not None:
            vals['HasCustomerCalled'] = self.HasCustomerCalled
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.IssueId is not None:
            vals['IssueId'] = self.IssueId
        if self.LastUpdated is not None:
            vals['LastUpdated'] = self.LastUpdated
        if self.LastUpdatedBy is not None:
            vals['LastUpdatedBy'] = self.LastUpdatedBy
        if self.Ordering is not None:
            vals['Ordering'] = self.Ordering
        if self.Priority is not None:
            vals['Priority'] = self.Priority
        if self.Stage is not None:
            vals['Stage'] = self.Stage
        if self.Summary is not None:
            vals['Summary'] = self.Summary
        if self.TargetCompletionDate is not None:
            vals['TargetCompletionDate'] = self.TargetCompletionDate
        if self.TicketApplication is not None:
            vals['TicketApplication'] = self.TicketApplication
        if self.TicketCategory is not None:
            vals['TicketCategory'] = self.TicketCategory
        if self.TicketTitle is not None:
            vals['TicketTitle'] = self.TicketTitle
        if self.TicketTypeId is not None:
            vals['TicketTypeId'] = self.TicketTypeId
        if self.TimeSpent is not None:
            vals['TimeSpent'] = self.TimeSpent
        if self.UserId is not None:
            vals['UserId'] = self.UserId
        return vals

    def _template(self):
        if self.CloseDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ContactId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.CreatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateCreated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DateInStage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.DevId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FolowUpDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.HasCustomerCalled: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.IssueId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdated: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastUpdatedBy: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Ordering: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Priority: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Stage: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Summary: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TargetCompletionDate: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TicketApplication: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TicketCategory: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TicketTitle: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TicketTypeId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.TimeSpent: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.UserId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class TicketStage(object):
    global ticketstages
    def __init__(self, values):
        self.values=values
        if 'ticketstages' not in globals():
            ticketstages = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'StageName' in values.keys():
            self.StageName=values['StageName']
        else:
            self.StageName=None

    def prepare(self):
        vals={}
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.StageName is not None:
            vals['StageName'] = self.StageName
        return vals

    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StageName: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class TicketType(object):
    global tickettypes
    def __init__(self, values):
        self.values=values
        if 'tickettypes' not in globals():
            tickettypes = []
        if 'CategoryId' in values.keys():
            self.CategoryId=values['CategoryId']
        else:
            self.CategoryId=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Label' in values.keys():
            self.Label=values['Label']
        else:
            self.Label=None

    def prepare(self):
        vals={}
        if self.CategoryId is not None:
            vals['CategoryId'] = self.CategoryId
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.Label is not None:
            vals['Label'] = self.Label
        return vals

    def _template(self):
        if self.CategoryId: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Label: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class User(object):
    global users
    def __init__(self, values):
        self.values=values
        if 'users' not in globals():
            users = []
        if 'City' in values.keys():
            self.City=values['City']
        else:
            self.City=None
        if 'Email' in values.keys():
            self.Email=values['Email']
        else:
            self.Email=None
        if 'EmailAddress2' in values.keys():
            self.EmailAddress2=values['EmailAddress2']
        else:
            self.EmailAddress2=None
        if 'EmailAddress3' in values.keys():
            self.EmailAddress3=values['EmailAddress3']
        else:
            self.EmailAddress3=None
        if 'FirstName' in values.keys():
            self.FirstName=values['FirstName']
        else:
            self.FirstName=None
        if 'HTMLSignature' in values.keys():
            self.HTMLSignature=values['HTMLSignature']
        else:
            self.HTMLSignature=None
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'LastName' in values.keys():
            self.LastName=values['LastName']
        else:
            self.LastName=None
        if 'MiddleName' in values.keys():
            self.MiddleName=values['MiddleName']
        else:
            self.MiddleName=None
        if 'Nickname' in values.keys():
            self.Nickname=values['Nickname']
        else:
            self.Nickname=None
        if 'Phone1' in values.keys():
            self.Phone1=values['Phone1']
        else:
            self.Phone1=None
        if 'Phone1Ext' in values.keys():
            self.Phone1Ext=values['Phone1Ext']
        else:
            self.Phone1Ext=None
        if 'Phone1Type' in values.keys():
            self.Phone1Type=values['Phone1Type']
        else:
            self.Phone1Type=None
        if 'Phone2' in values.keys():
            self.Phone2=values['Phone2']
        else:
            self.Phone2=None
        if 'Phone2Ext' in values.keys():
            self.Phone2Ext=values['Phone2Ext']
        else:
            self.Phone2Ext=None
        if 'Phone2Type' in values.keys():
            self.Phone2Type=values['Phone2Type']
        else:
            self.Phone2Type=None
        if 'PostalCode' in values.keys():
            self.PostalCode=values['PostalCode']
        else:
            self.PostalCode=None
        if 'Signature' in values.keys():
            self.Signature=values['Signature']
        else:
            self.Signature=None
        if 'SpouseName' in values.keys():
            self.SpouseName=values['SpouseName']
        else:
            self.SpouseName=None
        if 'State' in values.keys():
            self.State=values['State']
        else:
            self.State=None
        if 'StreetAddress1' in values.keys():
            self.StreetAddress1=values['StreetAddress1']
        else:
            self.StreetAddress1=None
        if 'StreetAddress2' in values.keys():
            self.StreetAddress2=values['StreetAddress2']
        else:
            self.StreetAddress2=None
        if 'Suffix' in values.keys():
            self.Suffix=values['Suffix']
        else:
            self.Suffix=None
        if 'Title' in values.keys():
            self.Title=values['Title']
        else:
            self.Title=None
        if 'ZipFour1' in values.keys():
            self.ZipFour1=values['ZipFour1']
        else:
            self.ZipFour1=None

    def prepare(self):
        vals={}
        if self.City is not None:
            vals['City'] = self.City
        if self.Email is not None:
            vals['Email'] = self.Email
        if self.EmailAddress2 is not None:
            vals['EmailAddress2'] = self.EmailAddress2
        if self.EmailAddress3 is not None:
            vals['EmailAddress3'] = self.EmailAddress3
        if self.FirstName is not None:
            vals['FirstName'] = self.FirstName
        if self.HTMLSignature is not None:
            vals['HTMLSignature'] = self.HTMLSignature
        if self.Id is not None:
            vals['Id'] = self.Id
        if self.LastName is not None:
            vals['LastName'] = self.LastName
        if self.MiddleName is not None:
            vals['MiddleName'] = self.MiddleName
        if self.Nickname is not None:
            vals['Nickname'] = self.Nickname
        if self.Phone1 is not None:
            vals['Phone1'] = self.Phone1
        if self.Phone1Ext is not None:
            vals['Phone1Ext'] = self.Phone1Ext
        if self.Phone1Type is not None:
            vals['Phone1Type'] = self.Phone1Type
        if self.Phone2 is not None:
            vals['Phone2'] = self.Phone2
        if self.Phone2Ext is not None:
            vals['Phone2Ext'] = self.Phone2Ext
        if self.Phone2Type is not None:
            vals['Phone2Type'] = self.Phone2Type
        if self.PostalCode is not None:
            vals['PostalCode'] = self.PostalCode
        if self.Signature is not None:
            vals['Signature'] = self.Signature
        if self.SpouseName is not None:
            vals['SpouseName'] = self.SpouseName
        if self.State is not None:
            vals['State'] = self.State
        if self.StreetAddress1 is not None:
            vals['StreetAddress1'] = self.StreetAddress1
        if self.StreetAddress2 is not None:
            vals['StreetAddress2'] = self.StreetAddress2
        if self.Suffix is not None:
            vals['Suffix'] = self.Suffix
        if self.Title is not None:
            vals['Title'] = self.Title
        if self.ZipFour1 is not None:
            vals['ZipFour1'] = self.ZipFour1
        return vals

    def _template(self):
        if self.City: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Email: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.EmailAddress3: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.FirstName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.HTMLSignature: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.LastName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.MiddleName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Nickname: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone1Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Ext: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Phone2Type: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.PostalCode: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Signature: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.SpouseName: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.State: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress1: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.StreetAddress2: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Suffix: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Title: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.ZipFour1: #is:
            #do Something
            pass
        else:
            #do something else
            pass



class UserGroup(object):
    global usergroups
    def __init__(self, values):
        self.values=values
        if 'usergroups' not in globals():
            usergroups = []
        if 'Id' in values.keys():
            self.Id=values['Id']
        else:
            self.Id=None
        if 'Name' in values.keys():
            self.Name=values['Name']
        else:
            self.Name=None
        if 'OwnerId' in values.keys():
            self.OwnerId=values['OwnerId']
        else:
            self.OwnerId=None


    def prepare(self):

                vals={}
                if self.Id is not None:
                    vals['Id'] = self.Id
                if self.Name is not None:
                    vals['Name'] = self.Name
                if self.OwnerId is not None:
                    vals['OwnerId'] = self.OwnerId

                return vals
    def _template(self):
        if self.Id: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.Name: #is:
            #do Something
            pass
        else:
            #do something else
            pass
        if self.OwnerId: #is:
            #do Something
            pass
        else:
            #do something else
            pass



