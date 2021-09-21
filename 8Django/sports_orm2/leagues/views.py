from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	context = {
		#7 todas las ligas con un jugador llamado Sophia
		"leagues": League.objects.filter(teams__curr_players__first_name = "Sophia"),
		# 1 todos los equipos de la Atlantic Soccer Conference
		# "teams": Team.objects.filter(league=League.objects.filter(name="Atlantic Soccer Conference")),
		# 6 todos los equipos con un jugador llamado Sophia
		# "teams": Team.objects.filter(curr_players__first_name="Sophia"),
		# 9 todos los equipos, pasados y presentes con los que Samuel Evans ha jugado
		#"teams": Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name = "Evans"),
		# 12 cada equipo para el que Jacob Gray jugo antes de unirse a los Oregon Colts
		#"teams": Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name = "Gray").exclude(team_name = "Colts", location = "Oregon"),
		# 14 todos los equipos que han tenido 12 o mas jugadores, pasados y presente
		"teams": Team.objects.annotate(x = Count('all_players')).filter(x__gt=11),
		# 2 todos los jugadores en los boston penquins
		# "players": Player.objects.filter(curr_team=Team.objects.filter(team_name="Penguins", location="Boston")),
		# 3 todos los jugadores en la international Collegiate baseball conference
		# "players": Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
		# 4 todos los jugadores en la conferencia Americana de Futbol Amateur con el apellido Lopez
		# "players": Player.objects.filter(curr_team__league__name = "American Conference of Amateur Football", last_name = "Lopez"),
		# 5 todos los jugadores de futbol
		# "players": Player.objects.filter(curr_team__league__sport = "Football"),
		# 8 todos con el apellido Flores que no jugan para los washington roughriders
		# "players": Player.objects.filter(last_name='Flores').exclude(curr_team__team_name = 'Roughriders', curr_team__location = 'Washington'),
		# 10 todos los jugadores, pasados y presentes de los Gatos tigre de manitoba
		# "players": Player.objects.filter(all_teams__team_name = "Tiger-Cats", all_teams__location = "Manitoba")
		# 11 todos los jugadores que anteriormente estaban con los Wichita Vikings
		# "players": Player.objects.filter(all_teams__team_name = "Vikings", all_teams__location = "Wichita").exclude(curr_team__team_name = "Vikings", curr_team__location = "Wichita"),
		# 13 todos llamados Joshua que alguna vez han jugado en la Federacion Atlantica de Jugadores de Beisbol Amateur
		# "players": Player.objects.filter(first_name = "Joshua", all_teams__league__name = "Atlantic Federation of Amateur Baseball Players"),
		# 15 todos los jugadores y el numero de equipos para los que jugo, ordenados por la cantidad de equipos para los que han jugado
		"players": Player.objects.annotate(x = Count('all_teams')).order_by('-x'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")