# class TestUser:
#     def setup(self):
#         self.new_user = User(1000)

#     def test_user_checklimit(self):
#         assert self.new_user.check_limit() == 0.0

#     def test_user_updatelimit_after_update(self):
#         self.new_user.update_limit(-100)
#         assert self.new_user.check_limit() == 100.0

#     def test_user_updatelimit_after_update_positive(self):
#         self.new_user.update_limit(100)
#         assert self.new_user.check_limit() == 0.0

#     def test_user_updatelimit_positive(self):
#         assert self.new_user.update_limit(-100) == 1

#     def test_user_updatelimit_negative(self):
#         print(self.new_user.current_limit)
#         assert self.new_user.update_limit(10000) == 0
