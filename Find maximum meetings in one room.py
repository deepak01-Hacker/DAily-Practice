    def __init__(self, start, end, pos):
         
        self.start = start
        self.end = end
        self.pos = pos
 
# Function for finding maximum 
# meeting in one room
def maxMeeting(l, n):
 
    # Initialising an arraylist 
    # for storing answer
    ans = []
     
    # Sorting of meeting according to
    # their finish time.
    l.sort(key = lambda x: x.end)
 
    # Initially select first meeting
    ans.append(l[0].pos)
 
    # time_limit to check whether new
    # meeting can be conducted or not.
    time_limit = l[0].end
     
    # Check for all meeting whether it
    # can be selected or not.
    for i in range(1, n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end
             
    # Print final selected meetings
    for i in ans:
        print(i + 1, end = " ")
         
    print()
