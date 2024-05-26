
#global variables
team=0
name=0
jersey=0
goals=0
lst=[]
teamdict={}
teams_list=[]

#main function
def main():
  while(True):
      x=int(input("New Entry - 1 \nDone and Exit - 2\n"))
      if x==1:
        team=str(input("Enter team Name: "))
        fname=str(input("Enter Player First Name: " ))
        lname=str(input("Enter Player Last Name: " ))
        jersey=int(input("Enter Jersey Number: "))
        goals=int(input("Enter Number of goals per season: "))
        a=(team,fname,lname,jersey,goals)
        lst.append(a)
      else:
        break

#TeamRoster function, prints the required output
def TeamRoster():
  #list by team name
  l2=[]
  for a in lst:
    l2.append(a[0])

  #sorting list
  l2.sort()

  lset=set(l2)
  for tname in lset:
    tl=[]
    for b in lst:
      if b[0]==tname:
        teamtuple=(b[0],b[1],b[2],b[3],b[4])
        tl.append(teamtuple)
    teams_list.append(tl)

  for team in teams_list:
    tname=str(team[0][0])
    j_no=[]
    sort_players=[]
    for ply in team:
      j_no.append(ply[3])
    j_no.sort()
    for no in j_no:
      for ply in team:
        if no==ply[3]:
          pay_tuple=(ply[1],ply[2],ply[3],ply[4])
          sort_players.append(pay_tuple)
    teamdict[tname]=sort_players
  print(teamdict)

#function for last name sort output
def LastNameSort():
  #last name sorted
  pl_lnames=[]
  for team in teamdict:
    for tm in teamdict[team]:
      pl_lnames.append(tm[1])
  pl_lnames.sort()

  lname_sorted=[]
  for lname in pl_lnames:
    for tl in teams_list:
      for ply in tl:
        if ply[2]==lname:
          print(ply[1],ply[2])

#function for sorting based on scores
def SocoringSort():
  #scoring list
  pl_score=[]
  for team in teamdict:
    for tm in teamdict[team]:
      pl_score.append(tm[3])
  pl_score.sort()

  lname_sorted=[]
  for lscore in pl_score:
    for tl in teams_list:
      for ply in tl:
        if ply[4]==lscore:
          print(ply)   

#function based on team ranking sort
def TeamRankSort():
  #Team Ranks
  tm_rank={}
  rank=[]
  for team in teamdict:
    goals=0
    for tm in teamdict[team]:
      goals+=int(tm[3])
    tm_rank[team]=goals
    rank.append(goals)

  rank.sort()
  for team in tm_rank:
    for r in rank:
      if tm_rank[team]==r:
        print(team+"->"+str(tm_rank[team]))


if __name__=="__main__":
  main()
  print("Team Roster output :")
  TeamRoster()
  print("sort by last name Output :")
  LastNameSort()
  print("sort by scoring output :")
  SocoringSort()
  print("sort by Team Ranks output :")
  TeamRankSort()
