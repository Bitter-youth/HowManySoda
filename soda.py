#coding:utf-8
class HowManySoda:
	#���
	price_of_drink = 2
	exchange_need_caps = 5
	exchange_need_bottles = 2

	#��Ʒ��
	money = 10
	drinks = 0
	bottles = 0
	caps = 0

	#�ȵ�ƿ��
	count = 0

	#������
	def buy(self):
		if self.money >= self.price_of_drink:
			self.money -= self.price_of_drink
			self.drinks += 1
			print('����ƿ��ˮ')
			return True
		return False
			
	#��ƿ�ǻ�����
	def ex_with_cap(self):
		if self.caps >= self.exchange_need_caps:
			self.caps -= self.exchange_need_caps
			self.drinks += 1
			print('��' + str(self.exchange_need_caps) + '��ƿ�ǻ���ƿ��ˮ')
			return True
		return False
			
	#��ƿ�ӻ�����
	def ex_with_bottle(self):
		if self.bottles >= self.exchange_need_bottles:
			self.bottles -= self.exchange_need_bottles
			self.drinks += 1
			print('��' + str(self.exchange_need_bottles) + '��ƿ�ӻ���ƿ��ˮ')
			return True
		return False
			
	#������
	def drink(self):
		if self.drinks > 0:
			self.drinks -= 1
			self.caps += 1
			self.bottles += 1
			self.count += 1
			print('����ƿ��ˮ')
			return True
		return False
			
	#���ƿ�ǻ�����
	def borrow_a_cap(self):
		if self.exchange_need_caps - self.caps == 1:
			print('���û��ѽ��˸�ƿ��')
			self.caps += 1
			self.ex_with_cap()
			self.drink()
			print('��ƿ�ǻ���������')
			self.caps -= 1
			return True
		return False

	#���ƿ�ӻ�����
	def borrow_a_bottle(self):
		if self.exchange_need_bottles - self.bottles == 1:
			print('���û��ѽ��˸�ƿ��')
			self.bottles += 1
			self.ex_with_bottle()
			self.drink()
			print('��ƿ�ӻ���������')
			self.bottles -= 1
			return True
		return False

if __name__ == '__main__':
	d = HowManySoda()
	d.money = input('�������Ľ�Ǯ����')
	d.price_of_drink = input('��ˮ����Ǯһƿ��')
	d.exchange_need_bottles = input('���ٸ�ƿ���ܻ�һƿ��ˮ��')
	d.exchange_need_caps = input('���ٸ�ƿ���ܻ�һƿ��ˮ��')
	print('��ʼ״̬��')
	print('��Ǯ: %d  ��ˮ: %d  ƿ��: %d  ƿ��:%d' % (d.money, d.drinks, d.bottles, d.caps))
	while d.buy() or d.drink() or d.ex_with_bottle() or d.ex_with_cap() or d.borrow_a_bottle() or d.borrow_a_cap():
		print('��Ǯ: %d  ��ˮ: %d  ƿ��: %d  ƿ��:%d' % (d.money, d.drinks, d.bottles, d.caps))
	print('�Ѿ����ܺȵ���ˮ�ˣ�һ������:'),
	print(d.count),
	print('ƿ')