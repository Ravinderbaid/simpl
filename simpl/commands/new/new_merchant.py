from ..cmd import Cmd
from model.merchant import Merchant


class CmdNewMerchant(Cmd):
    def process(self, name: str, email: str, discount: float) -> None:
        if not Merchant.instances.get(name):
            try:
                Merchant(name, email, discount)
                print(f"{name}({discount})")
            except Exception:
                del Merchant.instances[name]
                raise
        else:
            raise Exception("Merchant name already exist")
