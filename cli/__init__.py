from .src.cli import *
"""
    cli will 
        simple commands 
            -> date
                -> default: November 12, 1212 
                    -> can be changed to 
                        -> Nov 12, 1212
                        -> 12 Nov, 1212
                        -> Nov 12, 12 
                        -> 11 / 12 / 12 
            -> time
                -> default: 12:30 AM / PM [√]
                    -> can be changed to 
                        -> 24 hour format [√]
    
        auto deploy -> for this app
            -> will turn application into .exe and replace that in the .exe on the landing page for this panel

        file management
            -> create, read, update, and delete files in a specific directory 
            -> move or copy file or files to another directory
            -> convert file types (.txt, .json ) <- for now 

            -> modify .env variables (dev) options -> [project specific, global <- (dev machine)]
        
        package management -> will run 
            => auto update all packages --------> [yes, no])
            => show list of packages per language (globaly)
            => install a new package per language (globaly)
                [] 1.  -> node 
                [] 2.  -> python
                [] 3.  -> php      (if it exists)
                [] 4.  -> java     
                [] 5.  -> go
                [] 6.  -> C#       (if it exists)
                [] 7.  -> rust     
                [] 8.  -> swift    (if it exists)
                [] 10. -> kotlin   (if it exists)
                [] 11. -> scala    (if it exists)
                [] 12  -> groovy   (if it exists)
                [] 13. -> clojure  (if it exists)
                [] 14. -> lua      (if it exists)
                [] 15. -> elm      (if it exists)
                [] 16. -> fsharp   (if it exists)
                [] 17. -> dart     (if it exists)
                [] 18. -> julia    (if it exists)
                [] 19. -> haskell  (if it exists)
                [] 20. -> erlang   (if it exists)
"""