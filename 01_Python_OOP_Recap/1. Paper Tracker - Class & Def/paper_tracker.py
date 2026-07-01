#Project: CLI Research Log Manager
#This project was a way to revise python and work with class datatype again, before jumping into a course.

TARGET_PAPERS_PER_MONTH = 4

class ResearchPaper:
    def __init__(self, title : str, authors : str, year : int, finished : bool):
        self.title = title
        self.authors = authors
        self.year = year
        self.finished = finished
        self.summary: str = ""

    def __str__(self) -> str:
        status = 'Finished' if self.finished else 'Not Finished'
        summary = self.summary if self.summary else 'No summary added.'
        return f"{self.title} by {self.authors} ({self.year}) - {status}\n\nSummary: {summary}"
 
    def __eq__(self, other) -> bool:
        if not isinstance(other, ResearchPaper):
            return NotImplemented
        return other.title == self.title

    def add_summary(self, summary : str) -> None:
        self.summary = summary
    
    def mark_as_read(self) -> None:
        self.finished = True

def print_separator() -> None:
    print("--------------------------------------------------------------------------")

# Now that all the parameters are set, we can create a new ResearchPaper object and add it to the list of papers.

papers = [
    ResearchPaper("Deep Learning", "Ian Goodfellow, Yoshua Bengio, Aaron Courville", 2016, True)]

# Now that we have some examples, Let's create a menu for the user to interact with the program.
while True:
    print_separator()
    print("\nWelcome to the Research Paper Tracker!")
    print("Please select an option:")
    print("1. View all papers")
    print("2. Add a new paper")
    print("3. Mark a paper as read")
    print("4. Add a summary to a paper")
    print("5. Exit")
    print_separator()

    input_option = input("\nEnter your choice (1-5): ")

    if input_option == "1":
        print("\nHere are all the papers in your tracker:\n")
        for paper in papers:
            print_separator()
            print(paper)

        print_separator()
        
        print(f"\nYou have finished {sum(paper.finished for paper in papers)} papers till now. Your target is to read {TARGET_PAPERS_PER_MONTH} papers per month.")

    elif input_option == "2":
        title = input("\nEnter the title of the paper: ")
        authors = input("Enter the authors of the paper: ")

        while True:
            try:
                year = int(input("Enter the year of publication: "))
                break
            except ValueError:
                print("Please enter a valid year.")

        finished = input("Have you finished reading this paper? (y/n): ").lower() == 'y'
        print_separator()
        new_paper = ResearchPaper(title, authors, year, finished)
        if new_paper in papers:
            print("This Paper already exists")
        else:
            papers.append(new_paper)
            print(f"\n{new_paper.title} has been added to your tracker.")

    elif input_option == "3":
        title = input("\nEnter the title of the paper you want to mark as read: ")
        for paper in papers:
            if paper.title == title:
                paper.mark_as_read()
                print(f"\n{paper.title} has been marked as read.")
                break
        else:
            print(f"\n{title} was not found in your tracker.")

    elif input_option == "4":
        title = input("\nEnter the title of the paper you want to add a summary to: ")
        for paper in papers:
            if paper.title == title:
                summary = input("Enter the summary for the paper: ")
                paper.add_summary(summary)
                print(f"\nSummary added to {paper.title}.")
                break
        else:
            print(f"\n{title} was not found in your tracker.")

    elif input_option == "5":
        print("\nThank you for using the Research Paper Tracker. Goodbye!")
        break

    else:
        print("\nInvalid option. Please try again.")
