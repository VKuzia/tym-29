document.write(`
<nav class="navbar">
  <ul style="list-style-type:none;">
     <li><a href="index.html">Главная</a></li>
     <li><a href="tournaments.html">Турниры</a></li>
     <li>
        <div class="dropdown">
           <a>Подготовка</a>
           <div class="dropdown-content">
              <ul style="list-style-type:none;">
                 <li><a href="preparation/teamleads.html">Руководители</a></li>
                 <li><a href="preparation/written_materials.html">Оформление материалов</a></li>
                 <li><a href="preparation/quiz.html">Нулевой тур</a></li>
                 <li><a href="preparation/before_round.html">Перед боем</a></li>
                 <li><a href="preparation/round.html">Бой</a></li>
              </ul>
           </div>
        </div>
     </li>
     <li>
        <div class="dropdown">
           <a>Роли</a>
           <div class="dropdown-content">
              <ul style="list-style-type:none;">
                 <li><a href="roles/reporter/reporter.html">Докладчик</a></li>
                 <li><a href="roles/opponent/opponent.html">Оппонент</a></li>
                 <li><a href="roles/reviewer/reviewer.html">Рецензент</a></li>
                 <li><a href="roles/observer/observer.html">Наблюдатель</a></li>
                 <hr>
                 <li><a href="roles/roles.html">О ролях</a></li>
              </ul>
           </div>
        </div>
     </li>
     <li><a href="29.html">Гимназия №29</a></li>
</nav>
`);