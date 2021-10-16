# -*- coding: utf-8 -*-
# Created by Danil Sviridov

part1 = """<head>
	<link href='http://fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic,900italic,900' rel='stylesheet' type='text/css'>
	<style>
	    html {
	        background: #8962F8;
	    }
		.b1 {
  			position: absolute;
  			width: 500px;
  			height: 300px;
 	 		background: #8962F8;
		}

		.t1 {
  			position: absolute;
 			width: 500px;
  			height: 60px;

  			font-family: Roboto;
  			font-style: normal;
  			font-weight: bold;
  			font-size: 36px;
  			line-height: 30px;
  			text-align: center;
  			letter-spacing: 0.1px;

  			color: #FFFFFF;
		}

		.t2 {
			position: absolute;
			width: 134px;
			height: 30px;

			font-family: Roboto;
			font-style: normal;
			font-weight: bold;
			font-size: 36px;
			line-height: 30px;

			text-align: center;
			letter-spacing: 0.1px;
			margin-top: 5%;
			margin-left: 16%;

			color: #00160A;
		}

		.r1 {
			position: absolute;
			width: 200px;
			height: 50px;

			background: rgba(212, 212, 212, 0.7);
			border: 1px solid #000000;
			box-sizing: border-box;
			border-radius: 30px;
			margin-left: 30%;
			margin-top: 20%;
		}
		img {
			width: 309px;
			height: 309px;
			margin-left: 18%;
			margin-top: 10%;
		}
	</style>
</head>
<div class="b1 c1">
	<div class="d1">
		<a class="t1">Ваш одноразовый<br>пароль</a>
			<div class="r1">
				<a class="t2">"""
part2 = """</a>
			</div>
	</div>
	<img src="https://psv4.userapi.com/c532036/u592540045/docs/d18/fc85ed47f813/aaaaa.png?extra=DJOpJbfX8eCer2TCfccWdUz5S4J0jtVeqsWAXufXoCxpjhVHEKkWLJW-vJp5COI-TVupvRzZtwst8E5W7o4BV1PznhFrn4EKgLfIsS2sJ85WPPAVXU8zL8qNn0YRbMS1pz68uPzYuwPnT3G4xOH3jw26hw&dl=1">

</div>"""


def gen_mail(c):
    code = str(c)
    a = code[0] + code[1] + code[2]
    b = code[3] + code[4] + code[5]
    return part1 + a + ' ' + b + part2
