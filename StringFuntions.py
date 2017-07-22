
class StringFunctions:

	def __init__(self):
		"""
		Initiazing Method 
		"""
		pass
    def isPlindrome(self, string):
        """
        :param string: String to check if its palindrom or not, name should be lowercase
        :description: This functions checks string if its palindome series or not
        :return: boolean	
        """
        inversedName = "";
        for char in range(len(string)-1, -1, -1):
            inversedName += string[char]
        if(inversedName == string):
            return "true"
        else:
            return "false"
        del inversedName;




