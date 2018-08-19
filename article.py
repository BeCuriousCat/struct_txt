#coding=utf-8
import Toolbox
import re
import os


class article(object):
	num = 0


	def __init__(self, content, title,rule_list=None):
		self.title = title+'\n'
		self.child_list = []
		self.content = content.replace(' ', '')
		self.content = re.sub(r'^\s{1,}$', '', self.content)
		self.rule_list = []
		if rule_list == None:
			self.rule_list = Toolbox.readini("structT.ini")
		else:
			self.rule_list.extend(rule_list)
		self.word_count = len(self.content)
		if article.num == 0:
			self.Attribute = "root"
		elif self.content == self.title:
			self.Attribute = "bottom"
		else:
			self.Attribute = "child"
		article.num += 1
		try:
			self.get_par()
		except:
			pass

	def get_par(self):
		root_rule_list = []
		child_rule_list = []
		root_rule_list.extend(self.rule_list)
		for rule in root_rule_list:
			reg = re.compile((rule))
			par_title_list = reg.findall(self.content)
			if len(par_title_list) == 0:
				continue
			else:
				# child_rule_list.extend(root_rule_list[root_rule_list.index(rule)+1:])
				self.rule_list.remove(rule)
				break
		# print('\n'.join(par_title_list))
		if len(par_title_list) != 0 and par_title_list[0] != '':
			content_list = self.lspilt(par_title_list)
			if len(content_list) != 0 and content_list[0] != '':
				for content in content_list[1:]:
					temp = article(content, par_title_list[content_list[1:].index(content)],self.rule_list)
					self.add_child(temp)






	def add_child(self,child):
		self.child_list.append(child)

	def lspilt(self, poi_list):
		result_list = []
		content = self.content
		for poi in poi_list:
			# print(poi)
			# print(poi_list)
			# print(content)
			result_list.append(content.split(poi)[0])
			content = poi+content.split(poi)[1]
		result_list.append(content)
		return result_list

	def describe(self):
		print('文章标题:' + self.title.replace('\n', ''))
		print('文章字数:' + str(self.word_count))
		print("一级标题:"+str(len(self.child_list)))
		print([x.title for x in self.child_list])
		sec_list = []
		for x in self.child_list:
			sec_list = x.child_list + sec_list
		print("二级标题:"+ str(len(sec_list)))
		print([x.title for x in sec_list])

# #
# name_list = os.listdir('res/')
# num = 0
#
# for name in name_list:
# 	title = name.split('.')[0]
# 	content = Toolbox.readtxtfile("res/"+name)
# 	try:
# 		a = article(content, title)
# 	except:
# 		num = num + 1
# print("失败个数："+str(num))
# print("样本个数："+str(len(name_list)))
# print("错误率："+str(num/len(name_list)))



# title = "太原市人民政府关于印发太原市妇女发展“十一五”规划和儿童发展“十一五”规划的通知-太原市人民政府"
# content = Toolbox.readtxtfile('res/'+title + '.txt')
# a = article(content, title)
# a.describe()
# print(''.join([x.content for x in a.child_list]))



#
# for par in a.par_list:
# 	a.add_child
