#implement a classs called player that represents a cricket player
class player:
  def play(self):
    print("the player is playing cricket.")
    class batsman(player):
      def play(self):
        print("the batsman is bating.")
        class bowler(player):
          def play(self):
            print("the bowler is bowling.")
            batsman=batsman()
            bowler=bowler()
            batsman.play()
            bowler.play()
            