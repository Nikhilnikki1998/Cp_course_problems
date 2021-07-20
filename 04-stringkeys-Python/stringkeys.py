"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
    
    
    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        # a=calculate_hash_value(string)
        self.table.append(string)

        
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        if(string in self.table):
            return HashTable.calculate_hash_value(self,string)
        else:
            return -1
        

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hashvalue=0
        count=0
        for i in string:
            if(count==0):
                hashvalue+=ord(i)*100
                
            elif(count==1):
                hashvalue+=ord(i)
                break
            count=count+1
        
        return hashvalue

        # Your code goes here
        


