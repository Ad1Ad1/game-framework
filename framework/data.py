"""data.py"""
import json
from models import ErrorForm, ErrorHelper
import sys
import shutil
import os

class Database:
	def __init__(self, path, page, initial={}, sinit=False):
		asr=["page", "path to database", "initial data"]
		args=[page, path, initial]
		types=[str, str, dict]
		self.c=ErrorHelper(asr, args, types)
		self.pat=path
		self.p=page
		self.i=initial
		self.sinit=sinit
	
	def new(self):
		if self.c:
			return 1
		try:
			with open(self.pat, "w") as db:
				json.dump(self.i, db, indent=4)
			return 0
		except:
			ErrorForm(f"Could not create database {self.pat}: invalid file path", self.p, "102 DATABASE ERROR").call()
			self.c=True
			return 1
	
	def pageswap(self, pgnew):
		c=ErrorHelper(["page"], [pgnew], [str])
		if not self.c and not c:
			self.p=pgnew
			return 0
		return 1
	def change(self, name, to, total=False):
		c=ErrorHelper(["page", "total data marker"], [self.p, total], [str, bool])
		asr=["page", "field name"]
		args=[self.p, name]
		types=[str, str]
		if not c and not self.c:
				if total:
					asr.append("to")
					args.append(to)
					types.append(dict)
				if True:
					c=c or ErrorHelper(asr, args, types)
					if not c:
						data={}
						try:
							with open(self.pat, "r") as db:
								data=json.load(db)
						except FileNotFoundError:
							ErrorForm("Database file was not found. A new file will be created.", self.p, "102 DATABASE ERROR").call()
							self.new()
							if self.c:
								return 1
						if not total:
							try:
								data[name]=to
							except:
								ErrorForm(f"Field {name} is badly defined in this database.", self.p, "102 DATABASE ERROR").call()
								return 1
						with open(self.pat, "w") as db:
							if total:
								json.dump(to, db, indent=4)
							else:
								json.dump(data, db, indent=4)
							return 0
								
		return 1
		
	def retrieve(self, name, total=False):
			if self.c:
				return "ERR"
			asr=["page", "total data marker", "name"]
			args=[self.p, name, total]
			types=[str, str, bool]
			c=ErrorHelper(asr, args, types)
			if not c:
				dt={}
				err=False
				try:
					with open(self.pat, "r") as db:
						dt=json.load(db)
				except FileNotFoundError:
					if not self.sinit:
						ErrorForm("Database file was not found.",self.p, "102 DATABASE ERROR").call()
					err=True
				except json.JSONDecodeError:
					ErrorForm("Database file was not decoded properly.", self.p, "102 DATABASE ERROR").call()
					err=True
				if err:
					return "ERR"
				if total:
					return dt
				else:
					try:
						return dt[name]
					except:
						if not self.sinit:
							ErrorForm(f"Field {name} is badly defined in this database.", self.p, "102 DATABASE ERROR").call()
			return "ERR"
	def delete(self, name, total=False):
		c=ErrorHelper(["page", "total data marker"], [self.p, total], [str, bool])
		asr=["page", "field name"]
		args=[self.p, name]
		types=[str, str]
		if not c and not self.c:
				if True:
					c=c or ErrorHelper(asr, args, types)
					if not c:
						data={}
						try:
							with open(self.pat, "r") as db:
								data=json.load(db)
						except FileNotFoundError:
							ErrorForm("Database file was not found. A new file will be created.", self.p, "102 DATABASE ERROR").call()
							self.new()
							if self.c:
								return 1
						if not total:
							try:
								del data[name]
							except:
								ErrorForm(f"Field {name} is badly defined in this database.", self.p, "102 DATABASE ERROR").call()
								return 1
						with open(self.pat, "w") as db:
							if total:
								json.dump({}, db, indent=4)
							else:
								json.dump(data, db, indent=4)
							return 0
								
		return 1
	def upload(self, img):
		c=ErrorHelper(["page", "image file path"], [self.p, img], [str, str])
		if c:
			return 1
		strk=""
		for x in range(len(img)):
			if img[x]=="/":
				strk=""
			else:
				strk+=img[x]
		dest=f"./uploads/{strk}"
		os.makedirs("./uploads", exist_ok=True)
		try:
		    shutil.copy(img, dest)
		    return 0
		except FileNotFoundError:
		    ErrorForm(f"Invalid directory or file for upload.", self.p, type="104 UPLOAD ERROR").call()
		except PermissionError:
		    ErrorForm(f"Upload directory has an invalid permission setting. Please adjust the settings to proceed.", self.p, type="104 UPLOAD ERROR").call()
		return 1
