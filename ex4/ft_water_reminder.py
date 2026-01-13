# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lunsold <lunsold@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 16:47:46 by lunsold           #+#    #+#              #
#    Updated: 2026/01/13 17:54:26 by lunsold          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	days = int(input("Days since last watering: "))
	if(days > 2):
		print("Water the plants!")
	else:
		print("Plants are fine")
	pass
