CodeTypeArgs=('co_argcount', #int1
	'co_posonlyargcount',	#int2
	'co_kwonlyargcount',	#int3
	'co_nlocals',			#int4
	'co_stacksize',			#int5
	'co_flags',				#int6
	'co_code',				#bytes7
	'co_consts',			#tuple8
	'co_names',			    #tuple9
	'co_varnames',			#tuple10
	'co_filename',          #str11
	'co_name',				#str12
    'co_qualname',          #str13
	'co_firstlineno',		#int14
    'co_linetable',         #bytes15
	'co_lnotab',			#bytes16
	'co_freevars',			#tuple17
	'co_cellvars')          #tuple18
base_type = ("int", "float", "complex", "str", "bool")

base_collection = ("list", "tuple", "set", "frozenset", "bytearray", "bytes")
