METARESOURCES = ['datastructure', 'dataflow', 'codelist', 'conceptscheme', 'process']
FIELDS = {
    'TRACKING': ('class_name', 'id', 'created_by', 'changed_by', 'creation_date', 'changed_date'),
    'ANNOTATION': ('annotation_title', 'annotation_URL', 'annotation_text', 'id_code'),
}
FIELDS['ANNOTABLE'] = FIELDS['TRACKING'] + ('annotations',)
FIELDS['IDENTIFIABLE'] = FIELDS['ANNOTABLE'] + ('id_code', 'uri')
FIELDS['STRUCTURE_ITEM'] = FIELDS['IDENTIFIABLE'] + ('wrapper', 'concept')
FIELDS['NAMEABLE'] = FIELDS['IDENTIFIABLE'] + ('name', 'description')
FIELDS['ITEM'] = FIELDS['IDENTIFIABLE'] + ('wrapper',)
FIELDS['ITEMWITHPARENT'] = FIELDS['IDENTIFIABLE'] + ('wrapper', 'parent', 'depth')
FIELDS['VERSIONABLE'] = FIELDS['NAMEABLE'] + ('version', 'valid_from', 'valid_to')
FIELDS['MAINTAINABLE'] = FIELDS['VERSIONABLE'] + ('is_final', 'agency')
FIELDS['TEXTFORMAT'] = FIELDS['TRACKING'] + ('id_code', 'text_type', 'is_sequence', 'interval', 'start_value', 'end_value', 'time_interval', 'start_time', 'end_time', 'min_length', 'max_length', 'min_value', 'max_value', 'decimals', 'pattern', 'is_multiLingual') 
FIELDS['REPRESENTATION'] = FIELDS['TRACKING'] + ('text_format', 'enumeration', 'enumeration_format') 
FIELDS['CATEGORIZATION'] = FIELDS['MAINTAINABLE'] + ['source', 'target']
FIELDS['ATTACHMENTCONSTRAINT'] = FIELDS['MAINTAINABLE'] + ['attached2dsds', 'attached2dataflows', 'attached2datasets', 'attached2datasources', 'attached2provision', 'data_key_sets']
FIELDS['CONTENTCONSTRAINT'] = FIELDS['MAINTAINABLE'] + ['attached2dsds', 'attached2dataflows', 'attached2dataset', 'attached2datasource', 'attached2provision', 'periodicity', 'offset', 'tolerance', 'start_time', 'end_time', 'data_key_sets']
FIELDS['DATAKEYSET'] = FIELDS['TRACKING'] + ('attachment_constraint', 'content_constraint')
FIELDS['DATAKEY'] = FIELDS['TRACKING'] + ('data_key_set',)
FIELDS['KEYVALUE'] = FIELDS['TRACKING'] + ('data_key', 'dimension', 'attribute', 'code_value', 'string_value')
FIELDS['CUBEREGION'] = FIELDS['TRACKING'] + ('constraint', 'include')
FIELDS['KEYVALUESET'] = FIELDS['TRACKING'] + ('cube_region', 'dimension', 'attribute', 'code_values', 'string_values', 'start_time', 'end_time', 'start_inclusive', 'end_inclusive')
FIELDS['CODEVALUEDETAIL'] = FIELDS['TRACKING'] + ('code', 'key_value_set', 'cascade')
FIELDS['METAATTACHMENTCONSTRAINT'] = FIELDS['MAINTAINABLE'] + ['attached2metadsds', 'attached2metadataflows', 'attached2datasets', 'attached2datasources', 'attached2metaprovision', 'metadata_key_sets']
FIELDS['METACONTENTCONSTRAINT'] = FIELDS['MAINTAINABLE'] + ['attached2metadsds', 'attached2metadataflows', 'attached2dataset', 'attached2datasource', 'periodicity', 'offset', 'tolerance', 'start_time', 'end_time', 'metadata_key_sets']
FIELDS['METADATAKEYSET'] = FIELDS['TRACKING'] + ('metadata_key_set_code', 'attachment_constraint', 'content_constraint')
FIELDS['METADATAKEY'] = FIELDS['TRACKING'] + ('metadata_key_code', 'metadata_key_set', 'target', 'report')
FIELDS['METADATAKEYVALUE'] = FIELDS['TRACKING'] + ('metadata_key', 'target_component', 'value', 'data_set', 'data_key', 'objekt')
FIELDS['METADATATARGETREGION'] = FIELDS['TRACKING'] + ('metadata_target_region_code', 'target', 'report')
FIELDS['SIMPLEDATAKEY'] = FIELDS['TRACKING'] + ('simple_dim_key_code', 'dataflow')
FIELDS['SIMPLEDIMVALUE'] = FIELDS['TRACKING'] + ('simple_data_key', 'dimension', 'value')
FIELDS['METAKEYVALUESET'] = FIELDS['TRACKING'] + ('metadata_target_region', 'target_component', 'values', 'data_sets', 'data_keys', 'objects', 'start_time', 'end_time', 'start_inclusive', 'end_inclusive')
FIELDS['TIMEVALUE'] = FIELDS['TRACKING'] + ('time',)
FIELDS['METAATTRVALUESET'] = FIELDS['TRACKING'] + ('metadata_target_region', 'attribute', 'values', 'start_time', 'end_time', 'start_inclusive', 'end_inclusive')
FIELDS['DATAPARTIALKEY'] = FIELDS['TRACKING'] + ('data_partial_key_code', 'dataflow', 'attached_attrs') 
FIELDS['DATAPARTIALKEYVALUE'] = FIELDS['TRACKING'] + ('data_partial_key', 'dimension', 'value') 
FIELDS['DATAMEASUREKEY'] = FIELDS['TRACKING'] + ('data_measure_key_code', 'data_partial_key', 'measure_value', 'attached_attrs') 
FIELDS['DATAKEY'] = FIELDS['TRACKING'] + ('data_key_code', 'data_measure_key', 'time_value', 'attached_attrs') 
FIELDS['ATTRVALUEACTION'] = FIELDS['TRACKING'] + ('attr_value', 'dataflow', 'data_partial_key', 'data_measure_key', 'data_key', 'action')
FIELDS['OBS'] = FIELDS['TRACKING'] + ('data_key', 'value', 'action')
FIELDS['METADATATARGETKEY'] = FIELDS['TRACKING'] + ('metadata_flow', 'target', 'report', 'metadata_target', 'attached_attrs')
FIELDS['METAKEYVALUE'] = FIELDS['TRACKING'] + ('metadata_target_key', 'component', 'object_value', 'data_key_value', 'data_set_value', 'constraint_value', 'report_period_value')




