**Hack With Infy** 

Round 1 ---> Mode of Conduct - Online👨‍💻
3 Questions Easy, Medium, Kind of Medium with 50, 75, 100 marks respectively. 
I wasn't a good Programmer at the moment as I just started Programming but I managed to solve 1 problem of 75 Marks and got few points in 50 Marks one

(I wasnt expecting but cleared XD "crossed fingers lol")

Round 2 ---> Mode of Conduct - Online👨‍💻 31st May
3 Questions Medium, Hard, shit Hard :P  50,75,100 Marks
1st Problem was safe paths to find paths in a graph that can be visited avoiding the unwanted vertices
I used DFS

2nd Problem (Till this date I am trying to remember it :P) 75 Marks
We were not given Testcase so I am not sure how much TC's I must have passed but hope for good and 1 and a 1/2 problem is sufficient I guess.
HackwithInfy 


**INFYTQ**

ROUND 1 ---> Mode of Conduct - Online👨‍💻
Questions asked Aptitude, Python Programming (As I selected Python between Python and Java), DBMS, OOPS, DSA
Medium

Round 2 ---> Mode of Conduct - 👨‍💻It was supposed to be Onsite but due to Pandemic it was shifted on to an  Online Platform
14th June
Questions ---> 20 MCQS Python, DSA, DBMS, OOPS ---> 2 Codes

Problem Statement

1.Given an array and number of deletions delete the K number to get unique values.

Input  
2
1 2 3 3

Output
1

Explanation --> As we have 2 number of deletions 1 2 will be deleted and unique set is 3 so 1 unique number is present 
Hence Output is 1

My Solution in Python3

n,array=int(input()),list(map(int,input().split(" ")))
print(len(set([i[1]for i in sorted([[array.count(i),i] for i in array])[n:]]))) 

2.Alternate piece of vowels and consonants from word with min length 3 and max ASCII values

Input
greatness

Output
retes

Explanation : Picking up subsequence with vowel and consonant having maxium ASCII values

r --> consonants
e --> vowels
t --> consonants
e --> vowels
s --> consonants

My Solution in Python3

    s,ans,a,vowels= input(),"",[],['a','e','i','o','u']
    for i in s :
        a.append(1) if i in vowels else a.append(-1)    
    s1=s[0]

    for i in range (0, len(a)-1):

        if a[i]==a[i+1]:    
            s1+=s[i+1]
        else:ans+=max(s1);s1=s[i+1]
                              
    ans+=max(s1)
    
    if len(ans)>=3:
        print(ans)
    else: 
        print('X') 

On 14th June

I got mail 💌to have cleared both contest till 6 July and a Walkthrough for the positions happened at start of August.
I was waiting for my Interview since then but August totally went for Finale of Top 100 and PP Inteviews.
September too PP and SES Inteviews but still I did not get my Slot.
Well then on 6th October I received mail 💌my Interview to be scheduled on 14th October, I started preparing.
I was confident with Python and DSA a lot and OOPs, I wouldhv handled.
I skipped DBMS

On 14th It got cancelled XD🥺
(More time to prepare)

After 10 mails to HackwithInfy It got scheduled on 1st Dec and still did not happen🥺
Again it got rescheduled on 3rd December.

(Till here I was Comfortable with any CSE subject CN, OS, DAA, DBMS, OOPS, Programming, System Design) I studied everything

To my notice my Interview scheduled time was from 4 to 4.30 As Avg Interview span for a SES is 40 min.
(I wanted more time to speak) XD.

I logged in 3.45 Sharp (I am very punctual and only one thing I hate is being late)🤗 and My Interviewer also logged In at 3.50

recap on my Interviewer - He was VP and CTO at Infosys DA.
He had masters from University of Florida and He was Working on I guess technologies like RPA and Chatbots.
I wont be able to judge someone in 30 min but He was cool like me XD

I was wearing formals, white formal shirt, blue Tie and my Blazzer and ofcourse Jeans.
I wish I could wear Hoodie🤩
LOL wear something below even though it is online Interview.
I was looking like 😎Fat John wick with clean shave and without Guns:P

We Caugth up with Greetings and Formality, Very Formal Kinda I guess I got comfortable early.

then I was asked to show up my ID's I thinks it was for InfyTQ's Verification Process
Then we  spent some few minutes taking up screenshots as he was supposed to do that XD

then it started (This is cake part)🤓

My Introduction:

I told my name, my stream (I am Mechanical) and my CGPI.
My Interests
My Experiences during Internship
My Work in ARC
I have taught many student in my college from first year to third year from Robots to Python
I told about my Youtube channel, my subscriber count.
(" He said Good luck with that", so I am analyzing Interviews since 3 Months daily, I am Pro in this things, 
Even though he spoke nicely that was negative comment.)😔

He then asked me to wait so that he can pull up my Resume

(Also Smiling in Interview feels weird as hell)😛

As I mentioned my work with Manual Bots in my Intro he asked what competitions have you gone

Sumo Wrestling
Robo Soccer
Pick and Place I told him what it needs to be built that way.

He asked me is there something so that bot could detect Rock and Soccer during competitions
As my Bots were totally Manual I said its does not have any circuit only DPDT, my batteries and Me.

He then gave me a Situation How will you detect Obstacles 
I answered I worked on Ultrasonic and IR Sensors so using this we can detect Obstacles

He refactored Question and asked How a Rock and a Ball can be detected ?
I went on with Raspberry pi and pi Camera Module told I would use Open CV and Image Processing. (For me that was Satisfactory)
(I have some smart friends, every technology I know they taugth me. I learnt nothing in my school and college, Self Study is looob)

About my Internship as I worked as Quality Control and also as a DEVELOPER he asked me which you like the most.
Definitely I told my work as QCE and as DEVELOPER I get to learn more at my own pace and all that fluff stuff

Higher Studies?
I told I would like to work in and Industry, I feel that I would learn much more there.

In my Mind : Hell No, I can die but I will never go to some college now.

I dont remember exact but it came to problem solving and somehow to Datastructures He asked What all Data-Structures you know
Now I can list those that even u wont know but with nervousness I was just able to list basic Datastructures Linkedlist, Stack, Queues, Trees, Graphs
I said i have used them to solve problems reversal of string, linkedlist and all that.

HE questioned what Datastructures would u use to reverse a string your opinion no wrong or right answer here totally ur opinion

I said we could use stack and pop everylast element it will be good also we can use reverse linkedlist algorithm and that could do the job.

I studied DSA for much time the correct answer is Linkedlist let me elaborate.
stack might use extra contiguous space in memory and pop is shitty Idea
Reversal of linkedlist is good idea and setting up head pointer at Tail is pretty efficient
both take O(n) for Reversal

I wasnt able to explain in such way. If I was Interviewing myself I wont be satisfied.
He asked my Hobbies😄
I  told I am a speedcuber I visit Campuses to play in competitions he asked any other hobby
Like if u understand We already get so much less time how can we nurture our hobbies LOL 
I shouldhv said cooking, But my brain was running like pentium chip.
I became a nerd🤓.

I thing thats it guys then we moved to Any Questions part :

I asked "AS I was Interviewed for SE and SES through InfyTQ and HackwithInfy I was going through Hierarchy of those I doesnt match Why is that so ?"
Yeah I know pretty dope Question XD Tip --- Never ask their journey, They might already be bored 😒answering that question LOL
Also try not to ask your Performance directly you will get some boring answer😒.

He then asked me what do you mean by Hierarchy I told

SE --> SES --> PP --> Techlead --> Analyst
SES --> PP --> Enterprise Architect

He answered very detailed and properly.
For me Good Experience but very delayed, I learnt a lot this year and only because of Infosys, I hope I get SES there !! Pray for me YAll :)

I still feel I messed up a little could have been better if i got some Technical Questions
I studied every CSE subject but wasn't asked any of it :( 😞

I got result today on 9th December --> I AM SELECTED FOR SES from HackwithInfy

I received another mail for InfyTQ Upgradation test on 10th (Probably I cleared InfyTQ as well)
Exam is on 13th December and Pattern is same as HackwithInfy's 
