
# class TestMerchant:

#     def setup(self):
#         self.new_merchant = Merchant(1.25)

#     def test_update_discount_positive(self):
#         old_discount = self.new_merchant.discount
#         assert self.new_merchant.update_discount(
#             10) == "Updated discount from {}% to {}%".format(old_discount, 10)

#     def test_update_discount_negative(self):
#         try:
#             self.new_merchant.update_discount(0)
#             assert False
#         except ValidDiscountException as e:
#             assert e.message == "Invalid discount, discount cannot be less than 0"
