# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

import inspect
from typing import Iterable, Optional, Union

from marshmallow import EXCLUDE, fields  # type: ignore

from netapp_ontap.resource import Resource, ResourceSchema
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["ApplicationTemplate", "ApplicationTemplateSchema"]
__pdoc__ = {
    "ApplicationTemplateSchema.resource": False,
    "ApplicationTemplateSchema.patchable_fields": False,
    "ApplicationTemplateSchema.postable_fields": False,
}


class ApplicationTemplateSchema(ResourceSchema):
    """The fields of the ApplicationTemplate object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the application_template. """

    description = fields.Str(
        data_key="description",
    )
    r""" Description. """

    maxdata_on_san = fields.Nested("netapp_ontap.models.maxdata_on_san.MaxdataOnSanSchema", data_key="maxdata_on_san", unknown=EXCLUDE)
    r""" The maxdata_on_san field of the application_template. """

    missing_prerequisites = fields.Str(
        data_key="missing_prerequisites",
    )
    r""" Missing prerequisites. """

    mongo_db_on_san = fields.Nested("netapp_ontap.models.mongo_db_on_san.MongoDbOnSanSchema", data_key="mongo_db_on_san", unknown=EXCLUDE)
    r""" The mongo_db_on_san field of the application_template. """

    name = fields.Str(
        data_key="name",
    )
    r""" Template name. """

    nas = fields.Nested("netapp_ontap.models.nas.NasSchema", data_key="nas", unknown=EXCLUDE)
    r""" The nas field of the application_template. """

    nvme = fields.Nested("netapp_ontap.models.zapp_nvme.ZappNvmeSchema", data_key="nvme", unknown=EXCLUDE)
    r""" The nvme field of the application_template. """

    oracle_on_nfs = fields.Nested("netapp_ontap.models.oracle_on_nfs.OracleOnNfsSchema", data_key="oracle_on_nfs", unknown=EXCLUDE)
    r""" The oracle_on_nfs field of the application_template. """

    oracle_on_san = fields.Nested("netapp_ontap.models.oracle_on_san.OracleOnSanSchema", data_key="oracle_on_san", unknown=EXCLUDE)
    r""" The oracle_on_san field of the application_template. """

    oracle_rac_on_nfs = fields.Nested("netapp_ontap.models.oracle_rac_on_nfs.OracleRacOnNfsSchema", data_key="oracle_rac_on_nfs", unknown=EXCLUDE)
    r""" The oracle_rac_on_nfs field of the application_template. """

    oracle_rac_on_san = fields.Nested("netapp_ontap.models.oracle_rac_on_san.OracleRacOnSanSchema", data_key="oracle_rac_on_san", unknown=EXCLUDE)
    r""" The oracle_rac_on_san field of the application_template. """

    protocol = fields.Str(
        data_key="protocol",
        validate=enum_validation(['nas', 'nvme', 'san']),
    )
    r""" Access protocol.

Valid choices:

* nas
* nvme
* san """

    san = fields.Nested("netapp_ontap.models.san.SanSchema", data_key="san", unknown=EXCLUDE)
    r""" The san field of the application_template. """

    sql_on_san = fields.Nested("netapp_ontap.models.sql_on_san.SqlOnSanSchema", data_key="sql_on_san", unknown=EXCLUDE)
    r""" The sql_on_san field of the application_template. """

    sql_on_smb = fields.Nested("netapp_ontap.models.sql_on_smb.SqlOnSmbSchema", data_key="sql_on_smb", unknown=EXCLUDE)
    r""" The sql_on_smb field of the application_template. """

    vdi_on_nas = fields.Nested("netapp_ontap.models.vdi_on_nas.VdiOnNasSchema", data_key="vdi_on_nas", unknown=EXCLUDE)
    r""" The vdi_on_nas field of the application_template. """

    vdi_on_san = fields.Nested("netapp_ontap.models.vdi_on_san.VdiOnSanSchema", data_key="vdi_on_san", unknown=EXCLUDE)
    r""" The vdi_on_san field of the application_template. """

    vsi_on_nas = fields.Nested("netapp_ontap.models.vsi_on_nas.VsiOnNasSchema", data_key="vsi_on_nas", unknown=EXCLUDE)
    r""" The vsi_on_nas field of the application_template. """

    vsi_on_san = fields.Nested("netapp_ontap.models.vsi_on_san.VsiOnSanSchema", data_key="vsi_on_san", unknown=EXCLUDE)
    r""" The vsi_on_san field of the application_template. """

    @property
    def resource(self):
        return ApplicationTemplate

    @property
    def patchable_fields(self):
        return [
            "links",
            "maxdata_on_san",
            "mongo_db_on_san",
            "nas",
            "nvme",
            "oracle_on_nfs",
            "oracle_on_san",
            "oracle_rac_on_nfs",
            "oracle_rac_on_san",
            "san",
            "sql_on_san",
            "sql_on_smb",
            "vdi_on_nas",
            "vdi_on_san",
            "vsi_on_nas",
            "vsi_on_san",
        ]

    @property
    def postable_fields(self):
        return [
            "links",
            "maxdata_on_san",
            "mongo_db_on_san",
            "nas",
            "nvme",
            "oracle_on_nfs",
            "oracle_on_san",
            "oracle_rac_on_nfs",
            "oracle_rac_on_san",
            "san",
            "sql_on_san",
            "sql_on_smb",
            "vdi_on_nas",
            "vdi_on_san",
            "vsi_on_nas",
            "vsi_on_san",
        ]

class ApplicationTemplate(Resource):
    r""" Application templates """

    _schema = ApplicationTemplateSchema
    _path = "/api/application/templates"
    @property
    def _keys(self):
        return ["name"]

    # pylint: disable=bad-continuation
    # pylint: disable=missing-docstring
    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves application templates.
### Query examples
The most useful queries on this API allows searches by name or protocol access. The following query returns all templates that are used to provision an Oracle application.<br/><br/>
```
GET /application/templates?name=ora*
```
<br/>Similarly, the following query returns all templates that support SAN access.<br/><br/>
```
GET /application/templates?protocol=san
```
### Learn more
* [`DOC /application`](#docs-application-overview)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)  # pylint: disable=no-member



    # pylint: disable=missing-docstring
    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves application templates.
### Query examples
The most useful queries on this API allows searches by name or protocol access. The following query returns all templates that are used to provision an Oracle application.<br/><br/>
```
GET /application/templates?name=ora*
```
<br/>Similarly, the following query returns all templates that support SAN access.<br/><br/>
```
GET /application/templates?protocol=san
```
### Learn more
* [`DOC /application`](#docs-application-overview)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)  # pylint: disable=no-member

    # pylint: disable=missing-docstring
    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an application template.
### Template properties
Each application template has a set of properties. These properties are always nested under a property with the same name as the template. For example, when using the `mongo_db_on_san` template, the properties are found nested inside the `mongo_db_on_san` property. The properties nested under the template property are all specific to the template. The model for the application template object includes all the available templates, but only the object that corresponds to the template's name is returned, and only one is provided in any application API.<br/>
The model of each template includes a description of each property and its allowed values or usage. Default values are also indicated when available. The template properties returned by this API include an example value for each property.
### Template prerequisites
Each template has a set of prerequisites required for its use. If any of these prerequisites are not met, the `missing_prerequisites` property indicates which prerequisite is missing.
### Learn more
* [`DOC /application`](#docs-application-overview)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)  # pylint: disable=no-member





