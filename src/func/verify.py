class verify:
    @staticmethod
    def verifyNumType(n: str , base: int) -> bool:
        try:
            cleanNum = n.strip()
            int(cleanNum,base)
            return True
        except ValueError:
            return False

    @staticmethod
    def verifyNoNegOrDec(n:str) -> bool:
        cleanNum = n.strip()
        if ('-' in cleanNum or '.' in cleanNum):
            return False
        else:
            return True
        




