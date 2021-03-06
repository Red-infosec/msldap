#!/usr/bin/env python3
#
# Author:
#  Tamas Jos (@skelsec)
#

from datetime import datetime, timedelta, timezone
from msldap.ldap_objects.common import MSLDAP_UAC, vn


class MSADGPO:
	ATTRS = [ 	
		'cn', 'displayName', 'distinguishedName', 'flags', 'gPCFileSysPath', 
		'gPCFunctionalityVersion', 'gPCMachineExtensionNames', 'objectClass',
		'objectGUID', 'systemFlags', 'versionNumber', 'whenChanged', 'whenCreated',
	]

	def __init__(self):
		self.cn = None
		self.displayName = None
		self.distinguishedName = None
		self.flags = None
		self.gPCFileSysPath = None #str
		self.gPCFunctionalityVersion = None #str
		self.gPCMachineExtensionNames = None
		self.objectClass = None #str
		self.objectGUID = None #uid
		self.systemFlags = None #str
		self.whenChanged = None #uid
		self.whenCreated = None #str
		

	@staticmethod
	def from_ldap(entry, adinfo = None):
		adi = MSADGPO()
		adi.cn = entry['attributes'].get('cn') 
		adi.displayName = entry['attributes'].get('displayName')
		adi.distinguishedName = entry['attributes'].get('distinguishedName')
		adi.flags = entry['attributes'].get('flags')
		adi.gPCFileSysPath = entry['attributes'].get('gPCFileSysPath')
		adi.gPCFunctionalityVersion = entry['attributes'].get('gPCFunctionalityVersion')
		adi.gPCMachineExtensionNames = entry['attributes'].get('gPCMachineExtensionNames')
		adi.objectClass = entry['attributes'].get('objectClass')
		adi.objectGUID = entry['attributes'].get('objectGUID')
		adi.systemFlags = entry['attributes'].get('systemFlags')
		adi.whenChanged = entry['attributes'].get('whenChanged')
		adi.whenCreated = entry['attributes'].get('whenCreated')

		return adi

	def to_dict(self):
		t = {}
		t['cn'] = vn(self.cn)
		t['displayName'] = vn(self.displayName)
		t['distinguishedName'] = vn(self.distinguishedName)
		t['flags'] = vn(self.flags)
		t['gPCFileSysPath'] = vn(self.gPCFileSysPath)
		t['gPCFunctionalityVersion'] = vn(self.gPCFunctionalityVersion)
		t['gPCMachineExtensionNames'] = vn(self.gPCMachineExtensionNames)
		t['systemFlags'] = vn(self.systemFlags)
		t['objectClass'] = vn(self.objectClass)
		t['objectGUID'] = vn(self.objectGUID)
		t['whenChanged'] = vn(self.whenChanged)
		t['whenCreated'] = vn(self.whenCreated)
		return t

	def __str__(self):
		t = 'MSADUser\n'
		t += 'cn: %s\n' % self.cn 
		t += 'distinguishedName: %s\n' % self.distinguishedName 
		t += 'path: %s\n' % self.gPCFileSysPath 
		t += 'displayName: %s\n' % self.displayName 

		return t 

