#This script can be used to get the list of total submissions containing a given phrase in their title
#It will also result in the total upvote each submission got 
#At the end it will provide a summary about how many submissions were there containing the given phrase, their average upvotes and total upvotes overall
import praw

class SubmissionsByTitle:

    
    def __init__(self):
        self.total_upvotes = 0
        self.total_counts = 0
        self.subreddit_name = input("Enter the Subreddit Name : ")
        self.phrase = input("Enter the Keyword for the Titles : ")
        self.output_file = open("./output/output.txt",'w')
        self.phrase = self.phrase.strip()
        
        self.reddit = praw.Reddit(client_id = "u3HlJMzOxS8LCg", client_secret = "sNTYx5xyc2TGWqhsOl8fHSF_sK8", user_agent="Agent Virat")
        self.subreddit = self.reddit.subreddit(self.subreddit_name)
       

    def search_subreddit(self):
        for submission in self.subreddit.search(self.phrase,limit=None):
            try:
                # print(submission.title)
                # print(submission.score)
                # print("="*75)
                # print("\n")
                self.total_counts += 1
                self.total_upvotes += int(submission.score)
                self.output_file.write("TITLE : " + str(submission.title ) + "\n")
                self.output_file.write("UPVOTES : " + str(submission.score) + "\n\n")
                self.output_file.write("="*70 + "\n\n")
            except:
                continue

        self.output_file.write("TOTAL UPVOTES : " + str(self.total_upvotes) + "\n")
        self.output_file.write("TOTAL COUNTS : " + str(self.total_counts) + "\n")
        
        print("TOTAL UPVOTES : " + str(self.total_upvotes) + "\n")#not important
        print("TOTAL COUNTS : " + str(self.total_counts) + "\n")#not importatnt
        
        if self.total_counts == 0:
            self.close_everything()
            return
        
        self.output_file.write("AVERAGE UPVOTES : " + str(self.total_upvotes/self.total_counts) + "\n\n")
        self.output_file.write("="*100 + "\n\n")
        
        print("AVERAGE UPVOTES : " + str(self.total_upvotes/self.total_counts) + "\n\n")#not important
        self.close_everything()
            

    def randomSubmissions(self):
        #this can be used to check for average upvotes on a subreddit
        total_count = 0
        total_score = 0
        for i in range(500):
            submission = self.subreddit.random()
            print(submission.title)
            print(submission.score)
            total_count += 1
            total_score += int(submission.score)
            print("="*100)
        print("Average : " +  str(total_score/total_count))

    def close_everything(self):
        self.output_file.close()

obj = SubmissionsByTitle()
obj.search_subreddit()
# obj.randomSubmissions()
