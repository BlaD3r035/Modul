class verify:
    @staticmethod
    def verifyNumType(n: str , base: int):
        try:
            cleanNum = n.strip()
            int(n,base)
            return True
        except ValueError:
            return False




