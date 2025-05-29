from marshmallow import Schema, fields

class ContactDetailSchema(Schema):
    mobileCountryCode = fields.Str(required=True)
    mobileNumber = fields.Str(required=True)

class PostalAddressSchema(Schema):
    country = fields.Str(required=True)
    province = fields.Str(required=True)
    city = fields.Str(required=True)
    addressLine1 = fields.Str(required=True)
    addressLine2 = fields.Str(allow_none=True)
    addressLine3 = fields.Str(allow_none=True)
    postalCode = fields.Str(required=True)

class CustomerSchema(Schema):
    contactDetail = fields.Nested(ContactDetailSchema, required=True)
    postalAddress = fields.Nested(PostalAddressSchema, required=True)
    countryOfRegistration = fields.Str(required=True)
    emailAddress = fields.Email(required=True)
    establishmentDate = fields.Str(required=True)
    legalName = fields.Str(required=True)
    lineOfBusiness = fields.Str(required=True)
    registrationNumber = fields.Str(required=True)
    taxId = fields.Str(required=True)
    organizationType = fields.Str(allow_none=True)

class RoleSchema(Schema):
    id = fields.Int(required=True)
    alias = fields.Str(required=True)
    name = fields.Str(required=True)

class EntitySchema(Schema):
    postalAddress = fields.Nested(PostalAddressSchema, required=True)
    roles = fields.List(fields.Nested(RoleSchema), required=True)
    contactDetail = fields.Nested(ContactDetailSchema, required=True)
    tp = fields.Str(required=True)
    firstName = fields.Str(required=True)
    middleName = fields.Str(allow_none=True)
    lastName = fields.Str(required=True)
    birthDate = fields.Str(required=True)
    emailAddress = fields.Email(required=True)
    countryOfBirth = fields.Str(required=True)
    taxId = fields.Str(required=True)
    countryOfResidence = fields.Str(required=True)
    title = fields.Str(required=True)
    ownershipPercentage = fields.Int(required=True)
