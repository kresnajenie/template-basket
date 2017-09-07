import programTemplateBasket as sd
import argparse 
#import Gambar as gambar
# Soccer Player 
# Fungsi:
# 1. Ganti pemain
# 2. Line up
# 3. Stats

parser = argparse.ArgumentParser(description='Statistik Soccer')
parser.add_argument('--home', help='file team untuk home')
parser.add_argument('--away', help='file team untuk away')
parser.add_argument('--foto', help='file untuk foto player')

args=parser.parse_args()

team_home =  args.home
team_away= args.away
foto_filename = args.foto

#print team_home
#print team_away

sd.getMenuUtama(team_home,team_away,foto_filename)