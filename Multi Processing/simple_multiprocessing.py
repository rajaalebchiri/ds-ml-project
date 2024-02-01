# importing the multiprocessing module 
import multiprocessing
  
def first_function(name):
    """ 
    simple name print function
    """
    print(f"hello {name}")
  
def second_function(name):
    """ 
    simple print fucntion 
    """
    print(f"bonjour {name}")
  
if __name__ == "__main__":
    # creating processes 
    p1 = multiprocessing.Process(target=first_function, args=("john", )) 
    p2 = multiprocessing.Process(target=second_function, args=("david", )) 
  
    # starting process 1
    p1.start() 
    # starting process 2
    p2.start() 
  
    # wait until process 1 is finished
    p1.join() 
    # wait until process 2 is finished
    p2.join() 
  
    # both processes finished
    print("Done!") 