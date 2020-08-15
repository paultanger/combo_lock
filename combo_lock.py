'''
My partner Land keeps peeking at the lock combination, I can feel it! I just can't 
trust Land not to inspect the object or the source .py file and look at what the 
key I am comparing to is! But I have a plan. I would like to make the function 
that unlocks the lock have only content that I don't mind Land seeing. I know 
I can use the hash function (a builtin) to map an object to a number. I am thinking 
I could implement something like the code below. My implementation of these security 
features should not break any of Land's testing code and vice versa.

def open_lock(input):
return hash(str(input)+"you'll never find it Land!") == -7068180340459975452

#possible test code to show unit tests
print("Here is how we figure out what our hashed number should be: 
" + str(hash(str(1234)+"you'll never find it Land!")))
assert open_lock(1235) == False
assert open_lock(1234) == True

As Skylar suggested, hash the combination to prevent peeking
Ensure the user can only enter the code one digit at a time.
Implement checking to see if the digit entered is allowable (i.e, is a number 
and within the correct range). Determine how to deal with incorrect input 
(i.e, raise an error, use a default or coerced value, reject the input without 
an error, display an error message, etc)
Expand the number of allowable digits from 0-9 to 0-n.
Make it send you a text message if someone successfully opens your lock
Have it send a text message if someone attempts to open the lock X number of 
times and ask you to enable additional attempts.
'''
import secrets
import numpy as np

class ComboLock(object):
    def __init__(self, digits):
        self.digits = digits
        self.rng = secrets.SystemRandom()
        self.__code = self.__create_code()
        self.user_entered = ''
    
    def clear(self):
        '''
        clears the lock code and resets the lock
        '''
        self.user_entered = ''
        print('code has been reset')

    def __create_code(self):
        '''
        method to initialize lock code
        inputs number of digits
        sets instance code value
        '''
        # or use secret module?
        # set low limit
        self.low = 10 ** (self.digits-1)
        # set high limit
        self.high = 10 ** (self.digits)
        return self.rng.randint(self.low, self.high)
        #return randbelow(self.low, self.high)
        #return randint(0, self.digits)
        #return self.rng.integers(self.digits)
    
    def enter(self, n):
        '''
        accepts a numeric digit 0-9
        adds the digit to the code guess
        '''
        self.user_entered += str(n)
    
    def check_code(self):
        '''
        returns the digits the user has entered thus far
        '''
        print(f'the code you have entered is {self.user_entered}')
        return self.user_entered
    
    def print_code(self):
        '''
        for testing only
        '''
        #print(f'actual code is: {self.__code}')

    def open(self):
        '''
        tries to open the lock and if code matches returns true
        otherwise returns false
        '''
        if int(self.user_entered) == self.__code:
            print(' congratulations, you unlocked the lock')
            return True
        else:
            print('Sorry, that is not the correct code')
            return False
    
    def __repr__(self):
        return f'lock instance with {self.digits} digits in code'


if __name__ == '__main__':
    # print('running...')
    # lock = ComboLock(digits=4)
    # lock
    # # clear lock
    # lock.clear()
    # # enter code
    # lock.enter(1)
    # lock.enter(2)
    # lock.enter(3)
    # lock.enter(4)
    # # check entered code
    # lock.check_code()
    # # open lock
    # lock.open()




