from typing import Optional, List

from pydantic import BaseModel

from bexiopy.api.models import Search


class CountryBase(BaseModel):
    id: Optional[int]
    name: str
    name_short: str


class Country(CountryBase):
    iso_3166_alpha2: str


class CountryPost(CountryBase):
    iso3166_alpha2: str


class CountrySearch(Search):
    _allowed_search_fields: List[str] = ['name', 'name_short']


class Language(BaseModel):
    id: int
    name: str
    decimal_point: str
    thousands_separator: str
    date_format_id: int
    date_format: str
    iso_639_1: str


class LanguageSearch(Search):
    _allowed_search_fields = ['name', 'iso_639_1']


class NoteBase(BaseModel):
    id: Optional[int]
    user_id: int
    event_start: str
    subject: str
    info: str
    contact_id: int
    entry_id: Optional[int]
    module_id: Optional[int]


class Note(NoteBase):
    project_id: Optional[int]


class NotePost(NoteBase):
    pr_project_id: Optional[int]


class NoteSearch(Search):
    _allowed_search_fields = ['event_start', 'contact_id', 'user_id', 'subject', 'module_id', 'entry_id']


class CompanyProfile(BaseModel):
    id: Optional[int]
    name: Optional[str]
    address: Optional[str]
    address_nr: Optional[str]
    postcode: Optional[int]
    city: Optional[str]
    country_id: Optional[int]
    legal_form: Optional[str]
    country_name: Optional[str]
    mail: Optional[str]
    phone_fixed: Optional[str]
    phone_mobile: Optional[str]
    fax: Optional[str]
    url: Optional[str]
    skype_name: Optional[str]
    facebook_name: Optional[str]
    twitter_name: Optional[str]
    description: Optional[str]
    ust_id_nr: Optional[str]
    mwst_nr: Optional[str]
    trade_register_nr: Optional[str]
    has_own_logo: Optional[bool]
    is_public_profile: Optional[bool]
    is_logo_public: Optional[bool]
    is_address_public: Optional[bool]
    is_phone_public: Optional[bool]
    is_mobile_public: Optional[bool]
    is_fax_public: Optional[bool]
    is_mail_public: Optional[bool]
    is_url_public: Optional[bool]
    is_skype_public: Optional[bool]
    logo_base64: Optional[str]


class PaymentType(BaseModel):
    id: int
    name: str


class PaymentTypeSearch(Search):
    _allowed_search_fields = ['name']


class Payroll(BaseModel):
    activation: str


class LeanSync(BaseModel):
    activation: str


class Analytics(BaseModel):
    activation: str
    download: str


class FileUpload(BaseModel):
    activation: str
    edit: str
    show: str


class DocumentDesigner(BaseModel):
    activation: str


class Fm(BaseModel):
    activation: str


class AccountingReports(BaseModel):
    activation: str


class BillAdministration(BaseModel):
    activation: str


class UserAdministration(BaseModel):
    activation: str


class Admin(BaseModel):
    activation: str


class BankingDirect(BaseModel):
    activation: str


class BankingSync(BaseModel):
    activation: str


class Banking(BaseModel):
    activation: str
    edit: str


class Pingen(BaseModel):
    activation: str


class Mailchimp(BaseModel):
    activation: str


class Mailxpert(BaseModel):
    activation: str


class Gdrive(BaseModel):
    activation: str


class Boxnet(BaseModel):
    activation: str


class Dropbox(BaseModel):
    activation: str


class ProjectShowConditions(BaseModel):
    activation: str


class KbWizardV11(BaseModel):
    activation: str


class KbWizardReminder(BaseModel):
    activation: str


class KbWizardPayments(BaseModel):
    activation: str


class KbWizardRecurringInvoices(BaseModel):
    activation: str


class KbAccountStatement(BaseModel):
    activation: str
    edit: str
    show: str


class Expense(BaseModel):
    activation: str
    edit: str
    show: str


class KbBill(BaseModel):
    activation: str
    edit: str
    show: str


class KbArticleOrder(BaseModel):
    activation: str
    edit: str
    show: str


class KbDelivery(BaseModel):
    activation: str
    edit: str
    show: str


class KbCreditVoucher(BaseModel):
    activation: str
    edit: str
    show: str


class KbInvoice(BaseModel):
    activation: str
    edit: str
    show: str


class KbOrder(BaseModel):
    activation: str
    edit: str
    show: str


class KbOffer(BaseModel):
    activation: str
    edit: str
    show: str


class DashboardWidgetSales(BaseModel):
    activation: str


class FileManagerShare(BaseModel):
    activation: str


class Stockmanagement(BaseModel):
    activation: str
    edit: str
    show: str


class Monitoring(BaseModel):
    activation: str
    edit: str
    show: str


class Writer(BaseModel):
    activation: str
    edit: str
    show: str


class Article(BaseModel):
    activation: str
    edit: str
    show: str


class Project(BaseModel):
    activation: str
    edit: str
    show: str


class Marketing(BaseModel):
    activation: str
    edit: str
    show: str


class History(BaseModel):
    activation: str
    edit: str
    show: str


class Todo(BaseModel):
    activation: str
    edit: str
    show: str


class Calendar(BaseModel):
    activation: str
    edit: str
    show: str


class FileManager(BaseModel):
    activation: str
    edit: str
    show: str


class Contact(BaseModel):
    activation: str
    edit: str
    show: str


class StockmanagementChanges(BaseModel):
    edit: str


class Permissions(BaseModel):
    payroll: Payroll
    lean_sync: LeanSync
    analytics: Analytics
    file_upload: FileUpload
    document_designer: DocumentDesigner
    fm: Fm
    accounting_reports: AccountingReports
    bill_administration: BillAdministration
    user_administration: UserAdministration
    admin: Admin
    banking_direct: BankingDirect
    banking_sync: BankingSync
    banking: Banking
    pingen: Pingen
    mailchimp: Mailchimp
    mailxpert: Mailxpert
    gdrive: Gdrive
    boxnet: Boxnet
    dropbox: Dropbox
    project_show_conditions: ProjectShowConditions
    kb_wizard_v11: KbWizardV11
    kb_wizard_reminder: KbWizardReminder
    kb_wizard_payments: KbWizardPayments
    kb_wizard_recurring_invoices: KbWizardRecurringInvoices
    kb_account_statement: KbAccountStatement
    expense: Expense
    kb_bill: KbBill
    kb_article_order: KbArticleOrder
    kb_delivery: KbDelivery
    kb_credit_voucher: KbCreditVoucher
    kb_invoice: KbInvoice
    kb_order: KbOrder
    kb_offer: KbOffer
    dashboard_widget_sales: DashboardWidgetSales
    file_manager_share: FileManagerShare
    stockmanagement: Stockmanagement
    monitoring: Monitoring
    writer: Writer
    article: Article
    project: Project
    marketing: Marketing
    history: History
    todo: Todo
    calendar: Calendar
    file_manager: FileManager
    contact: Contact
    stockmanagement_changes: StockmanagementChanges


class UserPermission(BaseModel):
    components: List[str]
    permissions: Permissions
