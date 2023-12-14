def start_voting(participants):
    print("---------VOTING PHASE-----------------")
    votes = []
    for participant in participants:
        vote = int(input(f"Enter 1 if {participant} is ready to commit \nEnter 0 if {participant} is not ready to commit:\n"))
        votes.append(vote)
    return votes
def receive_commit(participant, prepared):
    if prepared:
        print(f"{participant} committed the transaction.")
    else:
        print(f"{participant} cannot commit. Not prepared.")
def send_commit(participants,votes):
    print("---------INDIVIDUAL LOGS----------------")
    for participant,vote in zip(participants,votes):
        receive_commit(participant,prepared=True) if vote==1 else receive_commit(participant,prepared=False)
def make_decision(votes):
    print("---------DECISION PHASE-----------------")
    if 0 in votes:
        print("Transaction aborted as all participating sites not ready!")
    else:
        print("Transaction successfully committed by all participants!")
num_participants = int(input("Enter the number of participants: "))
participants = []
for i in range(num_participants):
    participant = input("Enter participant name: ")
    participants.append(participant)
for participant in participants:
    print(f"{participant} is in Prepare Phase") #Prepare phase
votes = start_voting(participants)  # phase 1
send_commit(participants,votes)
make_decision(votes)  # phase 2
print("Transaction Completed!")
