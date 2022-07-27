from pydantic import BaseModel


class Contact(BaseModel):
    pass

"""
"id": 4,
"nr": "000001",
"contact_type_id": 1,
"name_1": "Example Company",
"name_2": null,
"salutation_id": 2,
"salutation_form": null,
"title_id": null,
"birthday": null,
"address": "Smith Street 22",
"postcode": 8004,
"city": "Zurich",
"country_id": 1,
"mail": "contact@example.org",
"mail_second": "",
"phone_fixed": "",
"phone_fixed_second": "",
"phone_mobile": "",
"fax": "",
"url": "",
"skype_name": "",
"remarks": "",
"language_id": null,
"is_lead": false,
"contact_group_ids": "1,2",
"contact_branch_ids": null,
"user_id": 1,
"owner_id": 1,
"updated_at": "2019-04-08 13:17:32",
"profile_image": "R0lGODlhAQABAIAAAAUEBAAAACwAAAAAAQABAAACAkQBADs="
"""