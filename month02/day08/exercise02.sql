create procedure p_in11(IN num int)
    begin
    select num;
    set num=100;
    select num;
end $$