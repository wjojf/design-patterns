# SRP SOC 
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos):
        del(self.entries[pos])
        self.count -= 1
    
    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    
    # def load_from_web(self):
    #     pass 
      
class FileManager:
    
    @staticmethod
    def save_to_file(instance, filename):
        with open(filename, 'w') as f:
            f.write(str(instance))
  
j = Journal()
j.add_entry('I ate a bug')
j.add_entry('Hello, world!')
FileManager.save_to_file(j, 'test.txt')
