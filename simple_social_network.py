# To get script from working directory to the local repository:
    # Add to the staging area for commiting, then commit it to the local repository:
        # run command: git add (insert file name here) and press Enter   <-- add it to the staging area
        # run command: git commit -m "(insert what was done to let partners know what was changed)"   <-- this will commit it to the local repository
# To share changes from local repository to partners:
    # run command: git push  <-- pushes to the remote repository where other people can work with it
        

""" A simple social network for tracking connections between people example """

class Person:
    """ A person in the social network. 
    
    Attributes:
        name (str): the person's name
        connections (set of Person): other people in the social network who know this person
    """

