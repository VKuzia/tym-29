document.write(`
<nav>
   <div class="navbar">
      <a href="index.html">Главная</a>
      <a href="tournaments.html">Турниры</a>
      <div class="dropdown">
         <button class="dropbtn">Подготовка</button>
         <div class="dropdown-content">
            <div>
               <a href="preparation/written_materials.html">Оформление материалов</a>
               <a href="preparation/quiz.html">Нулевой тур</a>
               <a href="preparation/before_round.html">Перед боем</a>
               <a href="preparation/round.html">Бой</a>
            </div>
         </div>
      </div>
      <div class="dropdown">
         <button class="dropbtn">Роли</button>
         <div class="dropdown-content">
            <a href="roles/reporter/reporter.html">Докладчик</a>
            <a href="roles/opponent/opponent.html">Оппонент</a>
            <a href="roles/reviewer/reviewer.html">Рецензент</a>
            <a href="roles/observer/observer.html">Наблюдатель</a>
            <hr>
            <a href="roles/roles.html">О ролях</a>
         </div>
      </div>
      <a href="29.html">Гимназия №29</a>
   </div>
</nav>
`);