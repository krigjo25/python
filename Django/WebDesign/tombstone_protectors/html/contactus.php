<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title> Contact us</title>
		<meta description="Tombstone Protector" />
		<meta name="author" content="thehtml5herald">
		<meta name="edited" content="@krigjo25" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="keywords" content="old timey newspaper, sports, businessinsiderprogram, ea, lgm">
		<meta http-equiv="content-security-policy|content-type|defult-style|refresh">
		<!-- Fonts used in this project -->
		<link href="https://fonts.googleapis.com/css2?family=Roboto&family=Rye&display=swap" rel="stylesheet" media="screen" />
		<!-- Cascade style sheets used to style the project-->
		<link rel="stylesheet" type="text/css" href="../css/index.css" media="screen" />
		<!-- Javascript used to style the project-->
		<script src="https://snapwidget.com/js/snapwidget.js"></script>
		<script src="https://kit.fontawesome.com/cb637e149e.js" crossorigin="anonymous"></script>
		<script type="../pfolio/javascript/polyfills/pholder.js"></script>
	</head>
	<body>
		<?php function daysFromNow($days) {
		$added = ($days * 24 * 3600) + time();
		return date("Y-m-d", $added);
	}?>

		<div id="curve">
			<header>
						<!-- 
							Headline - Dark brown shadow
							Logo - wildwest 
							navigation bar - old fashioned
						-->
				<h1>
					<span> The </span> 
					<a href="index.html"> Tombstone Protector 
						<!--<img src="../pfolio/logo/tmbpro.png" alt="(The Tombstone Protector Newspaper logo)">--></a>
					<br />
				</h1>
				<hr class="eight">
				<dl class="subtitle">
					<dt>
						<time datetime="2020-10-18 "> 
							<strong> 
								<i>18th,  October, 2020 </i>
							</strong>
						</time>
					</dt>
					<dt>
							<q>The Old West, A Time &amp; Place of The Heart </q>
					</dt>
					<dt> 
						<strong>
							<i>Volume VI</i>
						</strong>
					</dt>
				</dl>
				<hr>
				<nav>
					<!-- On click shift like papers-->
					<ul>
						<li>
							<a href="../html/index.html">Milestone</a>
						</li>
						<li>
							<a href="../html/sports.html">Sports</a>
						</li>
						<li>
							<a href="../html/business.html">Business</a>
						</li>
						<li>
							<a href="../html/enterart.html">Refreshments</a>
						</li>
						<li>
							<a href="../html/gentlelady.html">L&amp;G</a>
						</li>
						<li>
							<a href="../html/contactus.php"> Contact us</a>
						</li>
					</ul>
				</nav>
			</header>
			<main>
				<section>
					<h1> News / comments / feedbacks</h1>
						<p> Ea quo primis integre euripidis, an lorem iuvaret oportere qui. Vim vidit <span> docendi ne, eu deseruisse </span>intellegebat vim, ei virtute inermis mnesarchum cum. Ius gloriatur pertinacia interpretaris ex, congue platonem torquatos usu ne. Nec ad liber delicatissimi. Assum praesent recteque vix an, oblique quaerendum mel ex, pro quod tamquam elaboraret ea. Ius no vide pericula repudiare, ut est omnes ridens eruditi.</p>
				</section>
				<form id="register" method="post">
					<section>
						<ul>
							<li>
								<label for="name_reg"> Your name</label>
								<input type="text" id="name_reg" name="name" placeholder="e.g. Jhon Doe" required>
							</li>
							<li>
								<label for="e_add_reg">E-mail address :</label>
								<input type="email" id="e_add_reg" name="email" placeholder="e.g. example@domaine.com"required>
							</li>
							<li>
								<label for="telp"> Your phone number</label>
								<input type="tel" id="telp" name="telp" placeholder="e.g +47 12345678"pattern="\ ([2-9] {2}\ [0-9] {3} - [0-9] {4}">
							</li>
							<li>
								<label for="url"> Website :</label>
								<input type="url" id="url" name="url" placeholder="e.g. https://www.example.com">
							</li>
							<li>
								<label for="password"> desired password : </label>
								<input type="password" id="password" name="password" pattern="\S{6,10}" required>
							</li>
							<li>
								<label for="html_rate"> Your HTML knowledge 1 - 10</label>
								<input type="number" id="html_rate" name="html_rate" min="0" max="10" required>
							</li>
								<label for="subd"> Desired date to start Subscription</label>
								<input type="date" min="<?php echo (daysFromNow(1)); ?>" max="<?php echo (daysFromNow(91));?>" id="subd" name="subd" placeholder="<?php echo (daysFromNow(1)); ?>" required>
							</li>
							<li> <label for="quantity"> I would like to receive 
									<input type="number" id="quantity" name="quantity" min="0"> copies of 
									<cite>The Tombstone Protecture</cite>  
								</label>
							</li>
							<li>
								<label for="upsell"> Also Sign me up for
									<cite> The CSS3 Chronicle</cite>
								</label>
								<input type="checkbox" id="upsell" name="upsell" value="CSS Alexis Goldstein, Louis Lazaris, Estelle Weyl. HTML5 & CSS3 for the Real World (Kindle Locations 1101-1105). SitePoint Pty. Ltd.. ">
							</li>
							<li>
								<input type="submit" id="reg_submit" value="Send Post Haste">
							</li>
						</ul>
					</section>						
				</form>
				
			</main>
			<footer>
				<article id="aut">
					<p> Inspiration provided by <cite>
						<a href="https://www.sitepoint.com/premium/books/html5-css3-for-the-real-world-2nd-edition"> Sitepoint</a>'s,
						</cite> <a href="http://www.thehtml5herald.com" title="thehtml5herald.com">HTML &amp; CSS For the real world : The HTML Herald </a>
					</p>
					<p> Tombstone Protectors provided by: 
						<a href="https://www.krigjo25.com/certificates" title="Certificates">Web-Developer:</a> 
							<cite>
								<a href="https://www.krigjo25.com">@krigjo25</a>
							</cite>
					</p>
				</article>
				<ul>
				</ul>
				<nav id="somed">
					<ul>
						<li>
							<a href="https://www.facebook.com">
								<i class="fa fa-facebook-square" style="font-size:2em;" title="Facebook"> </i>
							</a>	
						</li>
						<li>
							<a href="https://www.instagram.com">
								<i class="fa fa-instagram" style="font-size:2em;" title="Instagram"></i>
							</a>
						</li>
						<li>
							<a href="https://github.com/krigjo25">
								<i class="fa fa-github-square" style="font-size: 2em" title="github"></i>
							</a>
						</li>
						<li>
							<a href="mailto:krigjo25@gmail.com ">
								<i class="fas fa-mail-bulk" style="font-size: 2em" title="Subscribe"></i>
							</a>
						</li>
					</ul> 
				</nav>
				<section>
					<small> no &copy;opyrights, Tombstone Protector Ltd.</small>
				</section>
			</footer>
		</div>
	</body>
</html>