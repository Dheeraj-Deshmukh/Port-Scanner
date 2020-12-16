# Port-Scanner


This is a port scanner which is built in python

Module dequired :- 
  * socket
  * IP   => pip3.6 install IPy
  *argparse
  
  How to use :-
   
   * -h and --help is for help
   * -t is for target either domain or ip both are acceptable
   * -p is for the range of the port it start with 1 and ends on the port which you describe with -p
    
              For Example :- python3.6 port_scanner -t www.abcd.com -p 1000
            
              This will search the open port between from 1 to 999 
    
   * -sc AND -cp | -sc is for starting range of the port and -cp for the closing range of the port 
    
             For Example :- python3.6 port_scanner -t www.abcd.com -sc 500 -cp 1000
            
              This will search the open port from 500 to 1000 
              
   
