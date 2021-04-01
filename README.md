目前有9张表：
ug1:user group 1，包含申请方的用户的id和密码
application:包含每条申请记录的时间，专利id，专利名称，专利所属类别（分三个层次），专利详情，申请人id，申请人名称
ref:weak entity of application，包含申请id和其中引用的其他专利的申请id
result:包含申请创建时间，受理时间，三个阶段的审批进度，最近一次汇总申请结果，审批通过时间，专利开始及结束时间，申请id，所有者姓名，所有者类型（公司？个体？）
reject_detail:weak entity of result,包含申请id，申请状态，受理时间，各项问题是否存在，针对各项问题拒绝申请引用的其他专利的数量
persoal_own:包含个人id，申请id（或许可以和result合并？）
company_own:包含专利所有人id，专利所有人在当时的公司id，申请id
person:模拟的外部表格，个人信息
company:模拟的外部表格，公司信息
下一步考虑:
0.创建ug2组审批人员
1.result添加审批人员id
2.新建内容库，将审批通过的专利名称，所有者和详细信息导入内容库,对通过审批的内容添加正式id
3.将所有者中的申请id替换为内容id（或者添加对应内容id）

