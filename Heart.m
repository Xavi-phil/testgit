syms x y z

f=(x^2+9/4*y^2+z^2-1)^3-x^2*z^3-9/80*y^2*z^3;

f=matlabFunction(f);

[x,y,z] = meshgrid(-1.5:.02:1.5,-1:.02:1,-1.5:.02:1.5);    % »­Í¼·¶Î§

v = f(x,y,z);

h = patch(isosurface(x,y,z,v,0));

isonormals(x,y,z,v,h)

set(h,'FaceColor','r','EdgeColor','none');

xlabel('x');ylabel('y');zlabel('z');

alpha(1)

grid on; view([1,1,1]); axis equal; camlight; lighting gouraud

axis off

pos1=get(gca,'position')

pos2=pos1;

pos2(2)=pos2(2)+0.01;

pos2(1)=pos2(1)-0.03;

pos2(3)=pos2(3)+0.08;

pos2(4)=pos2(4)+0.08;

for ii=1:10

    pause(1)

    set(gca,'position',pos1)

    pause(0.1)

    set(gca,'position',pos2)

    pause(0.1)

    set(gca,'position',pos1)

    pause(0.1)

    set(gca,'position',pos2)

    pause(0.1)

    set(gca,'position',pos1)

    pause(0.1)

    set(gca,'position',pos2)

    pause(0.1)

    set(gca,'position',pos1)

    pause(0.1)

    set(gca,'position',pos2)

    pause(0.1)

    set(gca,'position',pos1)

end