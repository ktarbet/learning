

import hydrofunctions as hf

site ='03250322'
rock_lick_cr = hf.NWIS(site,'iv',period='p10D')


print(rock_lick_cr.ok)
print(rock_lick_cr)
rock_lick_cr.df('temperature').head()
#rock_lick_cr.df('deg').plot()

pause = input("press enter to stop.")