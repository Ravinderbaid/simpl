from simpl.model.exceptions import EmailException, NameException
from simpl.model.customer import Customer


class TestClassCustomer:

    def test_customer_email(self):
        new_customer = Customer("ravinder", "ravinder@simpl.com")
        assert new_customer.email == "ravinder@simpl.com"

    def test_customer_set_email_negative(self):
        try:
            Customer("ravinder", "r@s.com")
            assert False
        except EmailException as e:
            assert e.args[0] == "Email format invalid. Expected: [<more_than_two_letter>@<more_than_three_letter>.<not_more_than_two_to_three_letter>]+(*All in small case)"

    def test_customer_name(self):
        new_customer = Customer("ravinder", "ravinder@simpl.com")
        assert new_customer.name == "ravinder"

    def test_customer_set_name_negative(self):
        try:
            Customer("r1234", "r@s.com")
            assert False
        except NameException as e:
            assert e.args[0] == "Name format invalid: name may only consist of letter"
