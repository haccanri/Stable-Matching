A simple python implementation of the Gale Shapley sorting algorithm.
Auto generates some males, females and their partner preferences. Then pairs them up according to the algorithm.

USAGE
python <file.py> [-v]

I recommend using -v for verbose output.

    #Gale Shapley Stable Matching algorithm
    Initially all m E M and w E W are free
    While there is a man m who is free and hasn't proposed to every woman
      Choose such a man m
      Let W be the highest-ranked woman in m's preference list to whom m has not yet proposed
      If W is free then
        (m, w) become engaged
      Else w is currently engaged to m'
        If w prefers m' to m then
          m remains free
        Else w prefers m to mt
          (m, w) become engaged
        mt becomes free
        Endif
      Endif
    Endwhile
    Return the set S of engaged pairs

